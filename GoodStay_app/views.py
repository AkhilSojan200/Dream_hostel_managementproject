from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from GoodStay_app.forms import StudentsForm, WardenForm, LoginForm


# Create your views here.


def index(request):
    return render(request, 'index.html')


def student_registration(request):
    student = StudentsForm()
    form1=LoginForm()
    if request.method=='POST':
        form=StudentsForm(request.POST)
        form1 = LoginForm(request.POST)
        if form1.is_valid() and form.is_valid():
           user=form1.save(commit=False)
           user.is_student=True
           user.save()
           user1 = form.save(commit=False)
           user1.user= user
           user1.save()
           return redirect("student_registration")
    return render(request,'student_registration.html',{'form':student,'form1':form1})



def warden_registration(request):
    form =  WardenForm()
    form2 = LoginForm()
    if request.method=='POST':
        form= WardenForm(request.POST)
        form2 = LoginForm(request.POST)

        if form2.is_valid() and form.is_valid():
           user=form2.save(commit=False)
           user.is_warden=True
           user.save()
           user2 = form.save(commit=False)
           user2.user1= user
           user2.save()
           return redirect("warden_registration")
    return render(request,'warden_regist.html',{'form':form,'form2':form2})


def login_page(request):
    if request.method =='POST':
        username= request.POST.get('uname')
        password= request.POST.get('pass')
        user= authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            if user.is_staff:
                return redirect('home_dashboard')
            elif user.is_student:
                return redirect('homestudent_dash')
            elif user.is_warden:
                return redirect('homewarden_dash')

    return render(request,'login_page.html')


def logout_temp(request):
    logout(request)
    return redirect('index')


# views.py
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

# Password reset views using Django's built-in system
class CustomPasswordResetView(auth_views.PasswordResetView):
    template_name = 'forgot_password.html'
    email_template_name = 'password_reset_email.html'
    subject_template_name = 'password_reset_subject.txt'
    success_url = reverse_lazy('password_reset_done')

class CustomPasswordResetDoneView(auth_views.PasswordResetDoneView):
    template_name = 'password_reset_done.html'

class CustomPasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    template_name = 'password_reset_confirm.html'
    success_url = reverse_lazy('password_reset_complete')

class CustomPasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    template_name = 'password_reset_complete.html'

