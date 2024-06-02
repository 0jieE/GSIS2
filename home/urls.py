from django.urls import path
from . import views,student_views, faculty_views

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
     path("administrator/class_schedule/enrollment",views.enrollment_class_schedule, name='enrollment_class_schedule-admin'),
     path("administrator/class_schedule/add",views.add_class_schedule, name='add-class_schedule-admin'),
     path('administrator/class_schedule/enrollment/<int:pk>/', views.erollment_class_schedule_report, name='enrollment_class_schedule-admin'),
     path('administrator/class_schedule/<int:pk>/edit/', views.edit_class_schedule, name='edit-class_schedule-admin'),
     path('administrator/class_schedule/<int:pk>/delete/', views.delete_class_schedule, name='delete-class_schedule-admin'),

     #prospectus
     path("administrator/prospectus/list",views.prospectus, name='prospectus-admin'),
     path("administrator/prospectus/add",views.add_prospectus, name='add-prospectus-admin'),
     path('administrator/prospectus/<int:pk>/edit/', views.edit_prospectus, name='edit-prospectus-admin'),
     path('administrator/prospectus/<int:pk>/delete/', views.delete_prospectus, name='delete-prospectus-admin'),

     #course_prospectus
     path("administrator/course_prospectus/list",views.course_prospectus, name='course_prospectus-admin'),
     path("administrator/course_prospectu/prospectus_list",views.prospectus_list, name='prospectus_list-admin'),
     path("administrator/course_prospectus/add",views.add_course_prospectus, name='add-course_prospectus-admin'),
     path('administrator/course_prospectus/<int:pk>/edit/', views.edit_course_prospectus, name='edit-course_prospectus-admin'),
     path('administrator/course_prospectus/<int:pk>/delete/', views.delete_course_prospectus, name='delete-course_prospectus-admin'),
     path('administrator/course_prospectus/report/<int:pk>/', views.course_prospectus_report, name='course_prospectus_report-admin'),

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
     path("administrator/subject_taken/grades",views.student_subject_taken_grade, name='subject_taken_grade-admin'),
     path("administrator/subject_taken/add",views.add_subject_taken, name='add-subject_taken-admin'),
     path('administrator/subject_taken/<int:pk>/edit/', views.edit_subject_taken, name='edit-subject_taken-admin'),
     path('administrator/subject_taken/<int:pk>/delete/', views.delete_subject_taken, name='delete-subject_taken-admin'),
     path('administrator/student_grade_report/<int:pk1>/<int:pk2>/', views.student_grade_report, name='student_grade_report-admin'),

     #Assessment
     path("administrator/assessment/list",views.assessment, name='assessment-admin'),
     path("administrator/assessment/add",views.add_assessment, name='add-assessment-admin'),
     path("calculate_fee_amount/", views.calculate_fee_amount, name='calculate-fee-amount'),
     path('administrator/assessment/<int:pk>/edit/', views.edit_assessment, name='edit-assessment-admin'),
     path('administrator/assessment/<int:pk>/delete/', views.delete_assessment, name='delete-assessment-admin'),

     #Payment
     path("administrator/payment/list",views.payment, name='payment-admin'),
     path("administrator/payment/add",views.add_payment, name='add-payment-admin'),
     path('administrator/payment/<int:pk>/edit/', views.edit_payment, name='edit-payment-admin'),
     path('administrator/payment/<int:pk>/delete/', views.delete_payment, name='delete-payment-admin'),

     #Student Profile
     path("administrator/student_profile/list",views.student_profile, name='student_profile-admin'),

# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    #####    #######  #     #   ######    ######  #     #   #######
   #     #      #     #     #   #     #   #       ##    #      #
   #            #     #     #   #     #   #       # #   #      #
    #####       #     #     #   #     #   ######  #  #  #      #
         #      #     #     #   #     #   #       #   # #      #
   #     #      #     #     #   #     #   #       #    ##      #
    #####       #      #####    ######    ######  #     #      #
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

     #grades
     path('student/grades/<int:pk>/', student_views.grades, name='grades'),
     path('student/grades/report/<int:pk>/', student_views.grades_report, name='grades-report'),
     path('student/grade/list',student_views.enrollment_grade_list,name='grade-list'),

     #class schedule
     path('student/class_schedule/<int:pk>/', student_views.class_schedules, name='class_schedule'),
     path('student/class_schedule/report/<int:pk>/', student_views.class_schedule_report, name='class_schedule-report'),
     path('student/class_schedule/list',student_views.enrollment_class_schedule_list,name='class_schedule-list'),

     #pre-enroll
     path('student/pre_enroll/', student_views.pre_enroll, name='pre_enroll'),
     path('subjects/<int:schedule_id_id>/pre-enroll/', student_views.pre_enroll_subject, name='pre_enroll-subject'),
     path('subjects/<int:pk>/removed/', student_views.delete_pre_enroll_subject, name='removed-subject'),

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
   #######      #       #####   #     #  #      #######   #      #
   #     #     # #     #     #  #     #  #         #       #    #
   #          #   #    #        #     #  #         #        #  #
   #####     #######   #        #     #  #         #         ##
   #         #     #   #        #     #  #         #         #
   #         #     #   #     #  #     #  #         #        #
   #         #     #    #####    #####   #######   #       #
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

     #grades
     path('faculty/grades/<int:pk>/', faculty_views.grades, name='faculty-grades'),
     path('faculty/grades/report/<int:pk>/', faculty_views.grades_report, name='faculty-grades-report'),
     path('faculty/edit_grade/<int:pk>/edit/', faculty_views.edit_grade, name='edit-grade'),
     path('faculty/grade/list',faculty_views.enrollment_grade_list,name='faculty-grade-list'),
     path('faculty/course_grade/<int:pk>/', faculty_views.course_grade, name='course_grade'),

     #class schedule
     path('faculty/class_schedule/<int:pk>/', faculty_views.faculty_class_schedules, name='faculty-class_schedule'),
     path('faculty/class_schedule/student_list/<int:pk>/', faculty_views.schedule_student_list, name='schedule_student_list'),
     path('faculty/class_schedule/report/<int:pk>/', faculty_views.faculty_class_schedule_report, name='faculty-class_schedule-report'),
     path('faculty/class_schedule_student_list/report/<int:pk>/', faculty_views.class_schedule_student_list_report, name='student_list-report'),
     path('faculty/class_schedule/list',faculty_views.faculty_class_schedule_list,name='faculty-class_schedule-list'),

]