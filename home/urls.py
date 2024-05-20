from django.urls import path
from . import views

urlpatterns = [
     path("",views.index,name='index'),

     # Authentication
     path('register-as-admin/', views.register_administrator, name='register-administrator'),
     path('register-as-staff/', views.register_staff, name='register-staff'),
     path('register-as-student/', views.register_student, name='register-student'),
     path("login/",views.login_view,name='login'),
     path('logout', views.logout_view, name='signout'),
     path('accounts/register/', views.UserRegistrationView.as_view(), name='register'),

     #pages
     path("administrator/home",views.administrator,name='admin-home'),
     path("staff/home",views.staff,name='staff-home'),
     path("student/home",views.student,name='student-home'),

     #College
     path("administrator/college/list",views.college, name='college-admin'),
     path("administrator/college/add",views.add_college, name='add-college-admin'),
     path('administrator/college/<int:pk>/edit/', views.edit_college, name='edit-college-admin'),
     path('administrator/college/<int:pk>/delete/', views.delete_college, name='delete-college-admin'),

     #department
     path("administrator/department/list",views.department, name='department-admin'),
     path("administrator/department/add",views.add_department, name='add-department-admin'),
     path('administrator/department/<int:pk>/edit/', views.edit_department, name='edit-department-admin'),
     path('administrator/department/<int:pk>/delete/', views.delete_department, name='delete-department-admin'),

     #course
     path("administrator/course/list",views.course, name='course-admin'),
     path("administrator/course/add",views.add_course, name='add-course-admin'),
     path('administrator/course/<int:pk>/edit/', views.edit_course, name='edit-course-admin'),
     path('administrator/course/<int:pk>/delete/', views.delete_course, name='delete-course-admin'),

     #enrollment
     path("administrator/enrollment/list",views.enrollment, name='enrollment-admin'),
     path("administrator/enrollment/add",views.add_enrollment, name='add-enrollment-admin'),
     path('administrator/enrollment/<int:pk>/edit/', views.edit_enrollment, name='edit-enrollment-admin'),
     path('administrator/enrollment/<int:pk>/delete/', views.delete_enrollment, name='delete-enrollment-admin'),

     #Room
     path("administrator/room/list",views.room, name='room-admin'),
     path("administrator/room/add",views.add_room, name='add-room-admin'),
     path('administrator/room/<int:pk>/edit/', views.edit_room, name='edit-room-admin'),
     path('administrator/room/<int:pk>/delete/', views.delete_room, name='delete-room-admin'),

     #subject
     path("administrator/subject/list",views.subject, name='subject-admin'),
     path("administrator/subject/add",views.add_subject, name='add-subject-admin'),
     path('administrator/subject/<int:pk>/edit/', views.edit_subject, name='edit-subject-admin'),
     path('administrator/subject/<int:pk>/delete/', views.delete_subject, name='delete-subject-admin'),

     #class schedule
     path("administrator/class_schedule/list",views.class_schedule, name='class_schedule-admin'),
     path("administrator/class_schedule/add",views.add_class_schedule, name='add-class_schedule-admin'),
     path('administrator/class_schedule/<int:pk>/edit/', views.edit_class_schedule, name='edit-class_schedule-admin'),
     path('administrator/class_schedule/<int:pk>/delete/', views.delete_class_schedule, name='delete-class_schedule-admin'),

     #prospectus
     path("administrator/prospectus/list",views.prospectus, name='prospectus-admin'),
     path("administrator/prospectus/add",views.add_prospectus, name='add-prospectus-admin'),
     path('administrator/prospectus/<int:pk>/edit/', views.edit_prospectus, name='edit-prospectus-admin'),
     path('administrator/prospectus/<int:pk>/delete/', views.delete_prospectus, name='delete-prospectus-admin'),

     #course_prospectus
     path("administrator/course_prospectus/list",views.course_prospectus, name='course_prospectus-admin'),
     path("administrator/course_prospectus/add",views.add_course_prospectus, name='add-course_prospectus-admin'),
     path('administrator/course_prospectus/<int:pk>/edit/', views.edit_course_prospectus, name='edit-course_prospectus-admin'),
     path('administrator/course_prospectus/<int:pk>/delete/', views.delete_course_prospectus, name='delete-course_prospectus-admin'),
]