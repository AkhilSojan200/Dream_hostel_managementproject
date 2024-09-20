from django.shortcuts import render,redirect
from django.http import HttpResponse

from GoodStay_app.forms import ComplaintsForm, ScheduleForm, NoticeForm
from GoodStay_app.models import RoomDetails, Complaints, Custom_warden, Schedule, Notification, Booking, Fee_payment


def warden_dashboard(request):
    return render(request, 'warden_templates/warden_dashboard.html')

def homewarden_dash(request):
    return render(request, 'warden_templates/homewarden_dash.html')


def wardenroom_view(request):
    wardenroom_view = RoomDetails.objects.all()
    return render(request, 'warden_templates/roomwarden_view.html', {'wardenviewroom':wardenroom_view})


def warden_complaint(request):
    complantwrden = ComplaintsForm()
    u = request.user

    if request.method == 'POST':
        form = ComplaintsForm(request.POST)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = u
            form.save()
            return redirect('warden_complaint')

    return render(request,"warden_templates/complaint_warden.html",{'hostlcomplaint':complantwrden})




def complaintwarden_view(request):
    complaint_warden_details = Complaints.objects.filter(user=request.user)
    return render(request, 'warden_templates/complaint_wardenview.html', {'wardenviewc':complaint_warden_details})




def schedulewarden_view(request):
    schedle_wardenview = Booking.objects.all()
    return render(request, 'warden_templates/wardensschedule_view.html', {'datetime':schedle_wardenview})



def notice_create(request):
    form = NoticeForm()
    if request.method == 'POST':
        form = NoticeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notice_create')
    return render(request, 'warden_templates/Wardennotice_create.html', {'form': form})




def notice_view(request):
    notice_details = Notification.objects.all()
    print(notice_details)
    return render(request, 'warden_templates/Wardennotice_view.html', {'noticeview': notice_details})


def notice_edit(request, upd):
    updatenotice = Notification.objects.get(id=upd)
    if request.method == 'POST':
        updateForm = NoticeForm(request.POST, request.FILES, instance=updatenotice)
        if updateForm.is_valid():
            updateForm.save()
            return redirect("notice_view")
    else:
        updateForm = NoticeForm(instance=updatenotice)
        return render(request, "warden_templates/Wardennotice_edit.html", {'general_notice': updateForm})



def notice_delete(request, dl):
    deletenotice = Notification.objects.get(id=dl)
    deletenotice.delete()
    return redirect("notice_view")

def viewstudent_payments(request):
    view_payments = Fee_payment.objects.all()
    return render(request, 'warden_templates/wardenview_feepayment.html', {'payments': view_payments})
