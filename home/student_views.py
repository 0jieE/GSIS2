from io import BytesIO
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string, get_template
from django.http import HttpResponse, JsonResponse
from xhtml2pdf import pisa
from .forms import LoginForm, StudentPreEnrollmentForm,SubjectTakenForm, AssessmentForm
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


#/////////////////////////////////////////
# pre_enroll
#////////////////////////////////////////

def pre_enroll(request):
    if not request.user.is_authenticated:
        return redirect("login")
    else:
        subject_taken = SubjectTaken.objects.all()
        class_schedules = Class_Schedule.objects.all()
        enrollment = Enrollment.objects.all()
        is_pre_enrolled = False
        try:
            enrollmentDetail = EnrollmentDetail.objects.get(student=request.user.id)
            found = True
        except EnrollmentDetail.DoesNotExist:
            found = False
        
        # Use the 'found' variable as needed in your view logic
        if found:
            is_pre_enrolled = True
            enrollment_detail_instance = enrollmentDetail
        else:
            is_pre_enrolled = False
            enrollment_detail_instance = None
        if request.method == "POST":
            if 'pre-enroll_student' in request.POST:
                form = StudentPreEnrollmentForm(request.POST)
                if form.is_valid():
                    form.save()
                    return redirect("pre_enroll")
            if 'pre-enroll_subject' in request.POST:
                    return redirect("pre_enroll-subject")
            if 'removed_subject' in request.POST:
                    return redirect("removed-subject")
        else:
            for e in enrollment:    
                if e.enrollment_ended == False:
                    enrollment_id = e
            student = request.user
            initial_data = {
            'student': student.id,
    
            'enrollment': enrollment_id.id,
            }
            form = StudentPreEnrollmentForm(initial=initial_data)
        context = {
              'parent':'',
              'segment':'pre-enroll',
              'form':form,
              'is_pre_enrolled':is_pre_enrolled,
              'enrollment':enrollment,
              'enrollment_id':enrollment_id,
              'class_schedules':class_schedules, 
              'subject_taken':subject_taken, 
              'enrollment_detail_instance':enrollment_detail_instance,
        }
        return render(request, 'student/pre_enrollment/pre_enroll.html',context)
    

def pre_enroll_subject(request, schedule_id_id):
    class_id = Class_Schedule.objects.get(pk=schedule_id_id)
    enrollment_detail_id = EnrollmentDetail.objects.get(student=request.user.id)
    SubjectTaken.objects.create(schedule_id = class_id, enrollment_detail_id=enrollment_detail_id,is_pre_enroll=True)
    return redirect('pre_enroll') 

def delete_pre_enroll_subject(request, pk):
    subject = get_object_or_404(SubjectTaken, pk=pk)
    if request.method == 'POST':
        subject.delete()
    return redirect('pre_enroll') 
    