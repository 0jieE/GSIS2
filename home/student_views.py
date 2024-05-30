from io import BytesIO
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string, get_template
from django.http import HttpResponse, JsonResponse
from xhtml2pdf import pisa
from .forms import LoginForm
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordResetConfirmView, PasswordResetView
from django.views.generic import CreateView
from django.contrib.auth import views as auth_views
from django.contrib.auth import logout, authenticate,login
from .models import College, Department, Course, Enrollment, Room, Subject, Class_Schedule, Prospectus, Course_Prospectus, SubjectTaken, Fees, Scholarship, EnrollmentDetail, SubjectTaken, Assessment, Payment
from django.contrib.auth.decorators import login_required

from .models import *


#///////////////////////////////////
# grades
#//////////////////////////////////
def enrollment_grade_list(request):
    if not request.user.is_authenticated:
        return redirect("login")
    else:
        enrollment = Enrollment.objects.all()
        context = {
              'parent':'',
              'segment':'grade',
              'enrollment':enrollment,     
        }
        return render(request, 'student/grades/enrollment_grades.html',context)

def grades(request,pk):
    if not request.user.is_authenticated:
        return redirect("login")
    else:
        subjects = Subject.objects.all()
        class_schedules = Class_Schedule.objects.all()
        subject_taken = SubjectTaken.objects.all()
        enrollment = Enrollment.objects.get(id=pk)
        students = Student_user.objects.get(id=request.user.id)
        enrollment_detail = EnrollmentDetail.objects.all()
        context = {
              'parent':'',
              'segment':'grade',
              'subject_taken':subject_taken,   
              'students':students,
              'enrollment':enrollment,
              'enrollment_detail':enrollment_detail, 
              'class_schedule':class_schedules,  
              'subjects':subjects,
        }
        return render(request, 'student/grades/grades.html',context)
    
def grades_report(request,pk):
    subjects = Subject.objects.all()
    class_schedules = Class_Schedule.objects.all()
    subject_taken = SubjectTaken.objects.all()
    enrollment = Enrollment.objects.get(id=pk)
    students = Student_user.objects.get(id=request.user.id)
    enrollment_detail = EnrollmentDetail.objects.all()
    context = {
            'parent':'',
            'segment':'grade',
            'subject_taken':subject_taken,   
            'students':students,
            'enrollment':enrollment,
            'enrollment_detail':enrollment_detail, 
            'class_schedule':class_schedules,  
            'subjects':subjects,
    }

    html = get_template('student/grades/grades_report.html').render(context)


    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'

    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

#/////////////////////////////////////////
# class schedule
#////////////////////////////////////////

def enrollment_class_schedule_list(request):
    if not request.user.is_authenticated:
        return redirect("login")
    else:
        enrollment = Enrollment.objects.all()
        context = {
              'parent':'',
              'segment':'class-schedule',
              'enrollment':enrollment,     
        }
        return render(request, 'student/class_schedule/enrollment_class_schedule.html',context)

def class_schedules(request,pk):
    if not request.user.is_authenticated:
        return redirect("login")
    else:
        course = Course.objects.all()
        subjects = Subject.objects.all()
        class_schedules = Class_Schedule.objects.all()
        subject_taken = SubjectTaken.objects.all()
        enrollment = Enrollment.objects.get(id=pk)
        students = Student_user.objects.get(id=request.user.id)
        enrollment_detail = EnrollmentDetail.objects.all()
        context = {
              'parent':'',
              'segment':'class-schedule',
              'subject_taken':subject_taken,   
              'students':students,
              'enrollment':enrollment,
              'enrollment_detail':enrollment_detail, 
              'class_schedule':class_schedules,  
              'subjects':subjects,
              'course':course,
        }  
        return render(request, 'student/class_schedule/class_schedule.html',context)
    
def class_schedule_report(request,pk):
    course = Course.objects.all()
    subjects = Subject.objects.all()
    class_schedules = Class_Schedule.objects.all()
    subject_taken = SubjectTaken.objects.all()
    enrollment = Enrollment.objects.get(id=pk)
    students = Student_user.objects.get(id=request.user.id)
    enrollment_detail = EnrollmentDetail.objects.all()
    context = {
            'parent':'',
            'segment':'grade',
            'subject_taken':subject_taken,   
            'students':students,
            'enrollment':enrollment,
            'enrollment_detail':enrollment_detail, 
            'class_schedule':class_schedules,  
            'subjects':subjects,
            'course':course,
    } 

    html = get_template('student/class_schedule/class_schedule_report.html').render(context)


    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'

    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response