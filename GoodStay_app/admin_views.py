from django.shortcuts import render,redirect
from django.http import HttpResponse

from GoodStay_app.forms import RoomDetailsForm, StudentsForm, WardenForm
from GoodStay_app.models import Custom_student, RoomDetails, Custom_warden, Complaints, Booking, Fee_payment


def admin_dashboard(request):
    return render(request, 'admin_templates/admin_dash.html')


def home_dashboard(request):
    return render(request, 'admin_templates/homeadmin.html')



def student_view(request):
    username_view = Custom_student.objects.all()
    print(username_view)
    return render(request, 'admin_templates/student_list.html', {'viewstudent':username_view})


def student_edit(request,up):
    updatestudent =Custom_student.objects.get(id=up)
    if request.method == 'POST':
        updateForm = StudentsForm(request.POST,  instance=updatestudent)
        if updateForm.is_valid():
            updateForm.save()
            return redirect("student_view")
    else:
        updateForm = StudentsForm(instance= updatestudent)
    return render(request, "admin_templates/edit_student.html", {'editstudent': updateForm})



def delete_student(request,dl):
    deltestdent = Custom_student.objects.get(id=dl)
    deltestdent.delete()
    return redirect("student_view")


def warden_view(request):
    userwarden_view = Custom_warden.objects.all()
    return render(request, 'admin_templates/warden_view.html', {'viewwarden':userwarden_view})


def warden_edit(request,upd):
    updatewarden =Custom_warden.objects.get(id=upd)
    if request.method == 'POST':
        updateForm = WardenForm(request.POST,  instance=updatewarden)
        if updateForm.is_valid():
            updateForm.save()
            return redirect("warden_view")
    else:
        updateForm = WardenForm(instance=updatewarden)
    return render(request, "admin_templates/edit_warden.html", {'editwarden': updateForm})



def delete_warden(request,dle):
    deltewarden = Custom_warden.objects.get(id=dle)
    deltewarden.delete()
    return redirect("warden_view")


# hostel room crud
def add_hostelroom(request):
    form = RoomDetailsForm()
    if request.method == 'POST':
        form = RoomDetailsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('add_hostelroom')
    return render(request, 'admin_templates/hostel_room.html', {'hostelcreate': form})

def room_view(request):
    adminroom_view = RoomDetails.objects.all()
    print("okkkkkk")
    for room in adminroom_view:
        print(room.Room_no)

    return render(request, 'admin_templates/room_view.html', {'viewroom': adminroom_view})


def room_edit(request,updte):
    updateroom =RoomDetails.objects.get(id=updte)
    if request.method == 'POST':
        updateForm = RoomDetailsForm(request.POST,  instance=updateroom)
        if updateForm.is_valid():
            updateForm.save()
            return redirect("room_view")
    else:
        updateForm = RoomDetailsForm(instance=updateroom)
    return render(request, "admin_templates/edit_room.html", {'editroom': updateForm})



def delete_room(request,dle):
    delteroom = RoomDetails.objects.get(id=dle)
    delteroom.delete()
    return redirect("room_view")

#complaint

def admin_complaintview(request):
    complaint_admin = Complaints.objects.all()
    return render(request, 'admin_templates/admin_complaintview.html', {'admincomplaint':complaint_admin})



def admin_complaintreply(request,id):
    complaintsreply =Complaints.objects.get(id=id)
    if request.method == 'POST':
        compltreply = request.POST.get('complaint_reply')
        complaintsreply.reply=compltreply
        complaintsreply.save()
        return redirect("admin_complaintview")

    return render(request, 'admin_templates/admin_complaintreply.html', {'replycomplaint': complaintsreply})



def viewstudent_roombook(request):
    studentroombook = Booking.objects.all()
    return render(request, 'admin_templates/adminview_roombook.html', {'roomviewstudent': studentroombook})


def accept(request, id):
    data = Booking.objects.get(id=id)
    data.status = 1
    data.save()
    return redirect('viewstudent_roombook')


def reject(request, id):
    data = Booking.objects.get(id=id)
    data.status = 2
    data.save()
    return redirect('viewstudent_roombook')

def view_payments(request):
    view_payment = Fee_payment.objects.all()
    return render(request, 'admin_templates/view_payments.html', {'payments': view_payment})


