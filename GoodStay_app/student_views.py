from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.http import HttpResponse

from GoodStay_app.forms import ComplaintsForm, ScheduleForm, FeePaymentForm
from GoodStay_app.models import RoomDetails, Complaints, Notification, Schedule, Custom_student, Booking, Custom_warden, \
    Fee_payment


def student_dashboard(request):
    return render(request, 'student_templates/student_dash.html')

def homestudent_dash(request):
    return render(request, 'student_templates/homestudent_dash.html')


def studentroom_view(request):
    studentroom_view = RoomDetails.objects.all()
    print(studentroom_view)

    return render(request, 'student_templates/roomstudent_see.html', {'studentviewroom':studentroom_view})


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

    return render(request,"student_templates/complaint_student1.html",{'studntcomplaint':complaint})

# complaint view or read


def complaint_viewstudent(request):
    complaints_details = Complaints.objects.filter(user=request.user)
    return render(request, 'student_templates/complain_studentview.html', {'viewcomplaint':complaints_details})


def studentnotice_view(request):
    view_notification = Notification.objects.all()
    return render(request, 'student_templates/Studentnotice_view.html', {'studentviewnotice':view_notification})



# schedule


def schedule_create(request):
    print("oke")
    createstudent_schedle = ScheduleForm()

    schedules = request.user
    print(request.user)
    student_schedule = Custom_student.objects.filter(name__iexact=request.user).first()

    if request.method == 'POST':
        form =ScheduleForm(request.POST)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.user=student_schedule
            obj.save()
            return redirect('schedulestudent_view')
    return render(request, 'student_templates/schedulestudent_create.html', {'form':createstudent_schedle})




def schedulestudent_view(request):
    student=Custom_student.objects.filter(name__iexact=request.user).first()
    bookings = Booking.objects.filter(user=student)

    return render(request, 'student_templates/schedulestudent_view.html', {'viewscdules': bookings})


def studentupdate_schedule(request,up):
    updateschedle =Schedule.objects.get(id=up)
    if request.method == 'POST':
        updateForm = ScheduleForm(request.POST,instance=updateschedle)
        if updateForm.is_valid():
            updateForm.save()
            return redirect("schedulestudent_view")
    else:
        updateForm = ScheduleForm(instance=updateschedle)
    return render(request, "student_templates/updatestudent_schedule.html", {'update_wardenschedule': updateForm})


def studentdelete_schedule(request,dle):
    deleteschedle = Schedule.objects.get(id=dle)
    deleteschedle.delete()
    return redirect("view_schedule")






# room booking
def room_booking(request, id):
    schedule = RoomDetails.objects.get(id=id)
    user = Custom_student.objects.get(name__iexact=request.user)

    if request.method == 'POST':
        # Get the input values for dates
        date_in = request.POST.get('date_in')
        date_out = request.POST.get('date_out')

        # Create a new booking object
        obj = Booking()
        obj.user = user
        obj.schedule = schedule
        obj.date_in = date_in
        obj.date_out = date_out
        obj.save()

        # Show a success message and redirect to the schedule view
        messages.info(request, 'Booked Successfully!')
        return redirect('schedulestudent_view')



    return render(request, 'student_templates/student_roombooking.html', {'bookstudent':schedule})



def view_room_booking(request):
    viewbook = Custom_student.objects.filter(name__iexact=request.user).first()
    book_view = Booking.objects.filter(user= viewbook)
    return render(request, 'student_templates/student_bookingview.html', {'bookroomview':book_view})


def view_hostelroom_booking(request):
    user=Custom_student.objects.get(name__iexact=request.user)
    print(user)
    book_hostel_details = Booking.objects.filter(user=user)
    print(book_hostel_details)
    return render(request, 'student_templates/studenthostelroom_book.html', {'bookingroom':book_hostel_details})

# Create fee payment

# def create_fee_payment(request):
#     if request.method == 'POST':
#         form = FeePaymentForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.info(request, 'Fee payment recorded successfully!')
#
#             return redirect('list_fee_payments')
#     else:
#         form = FeePaymentForm()
#     return render(request, 'student_templates/student_fee_payment.html', {'form': form})

def create_fee_payment(request):
    # Get the logged-in user's associated student record
    try:
        # Assuming Custom_student has a OneToOneField with User model
        custom_student = Custom_student.objects.get(user=request.user)  # or another field to identify the student
    except Custom_student.DoesNotExist:
        messages.error(request, 'You are not associated with any student record.')
        return redirect('some_error_page')  # Handle the error appropriately

    if request.method == 'POST':
        form = FeePaymentForm(request.POST)
        if form.is_valid():
            # Don't commit yet, you need to set the user (student) first
            fee_payment = form.save(commit=False)
            # Set the user (student) field based on the logged-in user
            fee_payment.user = custom_student  # Use the Custom_student instance
            fee_payment.save()
            messages.info(request, 'Fee payment recorded successfully!')
            return redirect('list_fee_payments')
    else:
        form = FeePaymentForm()

    return render(request, 'student_templates/student_fee_payment.html', {'form': form})


# def create_fee_payment(request):
#
#     fee_payment = FeePaymentForm()
#
#     payment = request.user
#     print(request.user)
#     student_schedule = Custom_student.objects.filter(name__iexact=request.user).first()
#
#     if request.method == 'POST':
#         form =FeePaymentForm(request.POST)
#         if form.is_valid():
#             obj=form.save(commit=False)
#             obj.user=student_schedule
#             obj.save()
#             return redirect('list_fee_payments')
#     return render(request, 'student_templates/student_fee_payment.html', {'form':fee_payment})
#

# @login_required
# def create_fee_payment(request):
#     # Get the logged-in user's associated student record
#     try:
#         student = Custom_student.objects.get(user=request.user)
#     except Custom_student.DoesNotExist:
#         messages.error(request, 'You are not associated with any student record.')
#         return redirect('some_error_page')  # Handle the error accordingly
#
#     if request.method == 'POST':
#         form = FeePaymentForm(request.POST)
#         if form.is_valid():
#             fee_payment = form.save(commit=False)
#             # Automatically set the user (student) field
#             fee_payment.user = student
#             fee_payment.save()
#             messages.info(request, 'Fee payment recorded successfully!')
#             return redirect('list_fee_payments')
#     else:
#         form = FeePaymentForm()
#
#     return render(request, 'student_templates/student_fee_payment.html', {'form': form})
#


# List all fee payments
def list_fee_payments(request):
    student = Custom_student.objects.filter(name__iexact=request.user).first()
    fee_payments = Fee_payment.objects.filter(user=student)

    # fee_payments = Fee_payment.objects.all()
    return render(request, 'student_templates/studentview_fee_payment.html', {'fee_payments': fee_payments})