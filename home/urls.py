from django.urls import path
from . import views

urlpatterns = [
     path("",views.index,name='index'),

     # Authentication
     path('signup/administrator/', views.register_administrator, name='register-administrator'),
     path('signup/staff/', views.register_staff, name='register-staff'),
     path('signup/faculty', views.register_faculty, name='register-faculty'),
     path('register-as-student/', views.register_student, name='register-student'),
     path("login/",views.login_view,name='login'),
     path('logout', views.logout_view, name='signout'),
     path('accounts/register/', views.UserRegistrationView.as_view(), name='register'),


     path('enroll/', views.enroll, name='enroll'),

     #user
     path('account/profile', views.user_profile, name='user-profile'),


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

     #Scholarship
     path("administrator/scholarship/list",views.scholarship, name='scholarship-admin'),
     path("administrator/scholarship/add",views.add_scholarship, name='add-scholarship-admin'),
     path('administrator/scholarship/<int:pk>/edit/', views.edit_scholarship, name='edit-scholarship-admin'),
     path('administrator/scholarship/<int:pk>/delete/', views.delete_scholarship, name='delete-scholarship-admin'),

     #Fees
     path("administrator/fees/list",views.fees, name='fees-admin'),
     path("administrator/fees/add",views.add_fees, name='add-fees-admin'),
     path('administrator/fees/<int:pk>/edit/', views.edit_fees, name='edit-fees-admin'),
     path('administrator/fees/<int:pk>/delete/', views.delete_fees, name='delete-fees-admin'),

     #Enrollment Detail
     path("administrator/enrollment_detail/list",views.enrollment_detail, name='enrollment_detail-admin'),
     path("administrator/enrollment_detail/add",views.add_enrollment_detail, name='add-enrollment_detail-admin'),
     path('administrator/enrollment_detail/<int:pk>/edit/', views.edit_enrollment_detail, name='edit-enrollment_detail-admin'),
     path('administrator/enrollment_detail/<int:pk>/delete/', views.delete_enrollment_detail, name='delete-enrollment_detail-admin'),

     #Subject Taken
     path("administrator/subject_taken/list",views.subject_taken, name='subject_taken-admin'),
     path("administrator/subject_taken/add",views.add_subject_taken, name='add-subject_taken-admin'),
     path('administrator/subject_taken/<int:pk>/edit/', views.edit_subject_taken, name='edit-subject_taken-admin'),
     path('administrator/subject_taken/<int:pk>/delete/', views.delete_subject_taken, name='delete-subject_taken-admin'),

     #Assessment
     path("administrator/assessment/list",views.assessment, name='assessment-admin'),
     path("administrator/assessment/add",views.add_assessment, name='add-assessment-admin'),
     path('administrator/assessment/<int:pk>/edit/', views.edit_assessment, name='edit-assessment-admin'),
     path('administrator/assessment/<int:pk>/delete/', views.delete_assessment, name='delete-assessment-admin'),

     #Payment
     path("administrator/payment/list",views.payment, name='payment-admin'),
     path("administrator/payment/add",views.add_payment, name='add-payment-admin'),
     path('administrator/payment/<int:pk>/edit/', views.edit_payment, name='edit-payment-admin'),
     path('administrator/payment/<int:pk>/delete/', views.delete_payment, name='delete-payment-admin'),

     #Student Profile
     path("administrator/student_profile/list",views.student_profile, name='student_profile-admin'),
]