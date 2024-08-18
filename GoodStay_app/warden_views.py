from django.shortcuts import render,redirect
from django.http import HttpResponse

from GoodStay_app.forms import ComplaintsForm, ScheduleForm, NoticeForm
from GoodStay_app.models import RoomDetails, Complaints, Custom_warden, Schedule, Notification


def warden_dashboard(request):
    return render(request, 'warden_dashboard.html')


def wardenroom_view(request):
    wardenroom_view = RoomDetails.objects.all()
    return render(request, 'roomwarden_view.html', {'wardenviewroom':wardenroom_view})


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

    return render(request,"complaint_warden.html",{'hostlcomplaint':complantwrden})




def complaintwarden_view(request):
    complaint_warden_details = Complaints.objects.filter(user=request.user)
    return render(request, 'complaint_wardenview.html', {'wardenviewc':complaint_warden_details})


def schedule_create(request):
    createwardn_schedle = ScheduleForm()
    schedules = request.user
    warden_schedle = Custom_warden.objects.filter(user1=schedules).first()
    # warden_schedle = Schedule.objects.filter(user1=value)
    if request.method == 'POST':
        form =ScheduleForm(request.POST)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.user=schedules
            obj.save()
            return redirect('schedule_create')
    return render(request, 'scheduleWarden_create.html', {'form':createwardn_schedle})




# def schedule_create(request):
#     form = ScheduleForm(request.POST)
#     if form.is_valid():
#         schedule = form.save(commit=False)
#         schedule.user1_id = request.user.id
#         schedule.save()
#         return redirect('schedule_create')
#     return render(request, 'scheduleWarden_create.html', {'form': form})




# def view_schedule(request):
#     warden=Custom_warden.objects.filter(user1=request.user).first()
#     schedules_details = Schedule.objects.filter(user=warden)
#     return render(request, 'schedulewarden_view.html', {'viewscdules': schedules_details})
#
#
# def wardenupdate_schedule(request,up):
#     updateschedle =Schedule.objects.get(id=up)
#     if request.method == 'POST':
#         updateForm = ScheduleForm(request.POST,instance=updateschedle)
#         if updateForm.is_valid():
#             updateForm.save()
#             return redirect("view_schedule")
#     else:
#         updateForm = ScheduleForm(instance=updateschedle)
#     return render(request, "updatewarden_schedule.html", {'update_wardenschedule': updateForm})
#
#
# def wardendelete_schedule(request,dle):
#     deleteschedle = Schedule.objects.get(id=dle)
#     deleteschedle.delete()
#     return redirect("view_schedule")



def notice_create(request):
    form = NoticeForm()
    if request.method == 'POST':
        form = NoticeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notice_create')
    return render(request, 'Wardennotice_create.html', {'form': form})




def notice_view(request):
    notice_details = Notification.objects.all()
    print(notice_details)
    return render(request, 'Wardennotice_view.html', {'noticeview': notice_details})


def notice_edit(request, upd):
    updatenotice = Notification.objects.get(id=upd)
    if request.method == 'POST':
        updateForm = NoticeForm(request.POST, request.FILES, instance=updatenotice)
        if updateForm.is_valid():
            updateForm.save()
            return redirect("notice_view")
    else:
        updateForm = NoticeForm(instance=updatenotice)
        return render(request, "Wardennotice_edit.html", {'general_notice': updateForm})



def notice_delete(request, dl):
    deletenotice = Notification.objects.get(id=dl)
    deletenotice.delete()
    return redirect("notice_view")



