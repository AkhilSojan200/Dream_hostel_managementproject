from django.urls import path
from . import views, admin_views, student_views, warden_views

urlpatterns = [

    path('', views.index, name='index'),
    path('student_registration',views.student_registration,name='student_registration'),
    path('warden_registration',views.warden_registration,name='warden_registration'),
    path('login_page', views.login_page, name='login_page'),
    path('logout', views.logout_temp, name='logout'),

    # admin url
    path('admin_dash', admin_views.admin_dashboard, name='admin_dashboard'),
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


    # student url

    path('student_dashboard', student_views.student_dashboard, name='student_dashboard'),
    path('studentroom_view', student_views.studentroom_view,name='studentroom_view'),
    path('complaintstudent', student_views.complaint_create, name='complaint_create'),
    path('complaint_view', student_views.complaint_viewstudent, name='complaint_viewstudent'),
    path('studentnotice_view', student_views.studentnotice_view,name='studentnotice_view'),





    # warden url

    path('warden_dashboard', warden_views.warden_dashboard, name='warden_dashboard'),
    path('wardenroom_view', warden_views.wardenroom_view,name='wardenroom_view'),
    path('complaint_warden', warden_views.warden_complaint,name='warden_complaint'),
    path('complaintwarden_view', warden_views.complaintwarden_view, name='complaintwarden_view'),
    path('schedule', warden_views.schedule_create, name='schedule_create'),
    # path('schedule_view', warden_views.view_schedule, name='view_schedule'),
    # path('update_schedule/<int:up>', warden_views.wardenupdate_schedule, name='wardenupdate_schedule'),
    # path('delete_schedule/<int:dle>', warden_views.wardendelete_schedule, name = 'wardendelete_schedule'),
    path('notice_create', warden_views.notice_create, name='notice_create'),
    path('notice_view', warden_views.notice_view, name='notice_view'),
    path('notice_edit/<int:upd>', warden_views.notice_edit, name='notice_edit'),
    path('notice_delete/<int:dl>', warden_views.notice_delete, name='notice_delete'),

]
