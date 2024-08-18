from django.shortcuts import render,redirect
from django.http import HttpResponse

from GoodStay_app.forms import ComplaintsForm
from GoodStay_app.models import RoomDetails, Complaints, Notification


def student_dashboard(request):
    return render(request, 'student_dashboard.html')

def studentroom_view(request):
    studentroom_view = RoomDetails.objects.all()
    return render(request, 'roomstudent_view.html', {'studentviewroom':studentroom_view})


def complaint_create(request):
    complaint = ComplaintsForm()
    u = request.user

    if request.method == 'POST':
        form = ComplaintsForm(request.POST)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = u
            form.save()
            return redirect('complaint_create')

    return render(request,"complaint_student1.html",{'studntcomplaint':complaint})

# complaint view or read


def complaint_viewstudent(request):
    complaints_details = Complaints.objects.filter(user=request.user)
    return render(request, 'complain_studentview.html', {'viewcomplaint':complaints_details})


def studentnotice_view(request):
    view_notification = Notification.objects.all()
    return render(request, 'Studentnotice_view.html', {'studentviewnotice':view_notification})
