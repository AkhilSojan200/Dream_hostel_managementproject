from django.urls import path
from . import views, admin_views, student_views, warden_views
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('', views.index, name='index'),
    path('student_registration',views.student_registration,name='student_registration'),
    path('warden_registration',views.warden_registration,name='warden_registration'),
    path('login_page', views.login_page, name='login_page'),
    path('logout', views.logout_temp, name='logout'),

 # Password reset URL patterns
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='forgot_password.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),



    # admin url
    path('admin_dash', admin_views.admin_dashboard, name='admin_dashboard'),
    path('home_dashboard', admin_views.home_dashboard, name='home_dashboard'),
    path('student_view', admin_views.student_view,name='student_view'),
    path('student_edit/<int:up>', admin_views.student_edit,name='student_edit'),
    path('delete_student/<int:dl>',admin_views.delete_student, name ='delete_student'),
    path('warden_view', admin_views.warden_view,name='warden_view'),
    path('warden_edit/<int:upd>', admin_views.warden_edit,name='warden_edit'),
    path('delete_warden/<int:dle>',admin_views.delete_warden, name ='delete_warden'),

    path('add_hostelroom', admin_views.add_hostelroom,name='add_hostelroom'),
    path('room_view', admin_views.room_view,name='room_view'),
    path('room_edit/<int:updte>', admin_views.room_edit,name='room_edit'),
    path('delete_room/<int:dle>',admin_views.delete_room, name ='delete_room'),
    path('admin_complaintview', admin_views.admin_complaintview, name='admin_complaintview'),
    path('complaint_reply/<int:id>', admin_views.admin_complaintreply, name='admin_complaintreply'),
    path('viewstudent_roombook', admin_views.viewstudent_roombook, name='viewstudent_roombook'),
    path('accept/<int:id>', admin_views.accept, name='accept'),
    path('reject/<int:id>', admin_views.reject, name='reject'),
    path('view_payments', admin_views.view_payments, name='view_payments'),


    # student url

    path('student_dashboard', student_views.student_dashboard, name='student_dashboard'),
    path('homestudent_dash', student_views.homestudent_dash, name='homestudent_dash'),
    path('studentroom_view', student_views.studentroom_view,name='studentroom_view'),
    path('complaintstudent', student_views.complaint_create, name='complaint_create'),
    path('complaint_view', student_views.complaint_viewstudent, name='complaint_viewstudent'),
    path('studentnotice_view', student_views.studentnotice_view,name='studentnotice_view'),

    path('schedule', student_views.schedule_create, name='schedule_create'),
    path('schedulestudent_view', student_views.schedulestudent_view, name='schedulestudent_view'),
    path('update_schedule/<int:up>', student_views.studentupdate_schedule, name='studentupdate_schedule'),
    path('delete_schedule/<int:dle>', student_views.studentdelete_schedule, name='studentdelete_schedule'),

    path('room_booking/<int:id>', student_views.room_booking, name='room_booking'),
    path('view_room_booking', student_views.view_room_booking, name='view_room_booking'),
    path('view_hostelroom_booking', student_views.view_hostelroom_booking, name='view_hostelroom_booking'),
    path('create_fee_payment', student_views.create_fee_payment, name='create_fee_payment'),
    path('list_fee_payments', student_views.list_fee_payments, name='list_fee_payments'),





    # warden url

    path('warden_dashboard', warden_views.warden_dashboard, name='warden_dashboard'),
    path('homewarden_dash', warden_views.homewarden_dash, name='homewarden_dash'),
    path('wardenroom_view', warden_views.wardenroom_view,name='wardenroom_view'),
    path('complaint_warden', warden_views.warden_complaint,name='warden_complaint'),
    path('complaintwarden_view', warden_views.complaintwarden_view, name='complaintwarden_view'),


    path('schedulewarden_view', warden_views.schedulewarden_view, name='schedulewarden_view'),
    path('notice_create', warden_views.notice_create, name='notice_create'),
    path('notice_view', warden_views.notice_view, name='notice_view'),
    path('notice_edit/<int:upd>', warden_views.notice_edit, name='notice_edit'),
    path('notice_delete/<int:dl>', warden_views.notice_delete, name='notice_delete'),
    path('viewstudent_payments', warden_views.viewstudent_payments, name='viewstudent_payments'),



]
