from io import BytesIO
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string, get_template
from django.http import HttpResponse, JsonResponse
from xhtml2pdf import pisa
from .forms import LoginForm,SubjectTakenForm, FacultyGradeForm
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
        return render(request, 'faculty/grades/enrollment_grades.html',context)

    
def course_grade(request,pk):
    if not request.user.is_authenticated:
        return redirect("login")
    else:
        course = Course.objects.all()
        subjects = Subject.objects.all()
        class_schedules = Class_Schedule.objects.all()
        subject_taken = SubjectTaken.objects.all()
        enrollment = Enrollment.objects.get(id=pk)
        faculty = Faculty_user.objects.get(id=request.user.id)
        enrollment_detail = EnrollmentDetail.objects.all()
        context = {
              'parent':'',
              'segment':'grade',
              'subject_taken':subject_taken,   
              'faculty':faculty,
              'enrollment':enrollment,
              'enrollment_detail':enrollment_detail, 
              'class_schedules':class_schedules,  
              'subjects':subjects,
              'course':course,
        }  
        return render(request, 'faculty/grades/course_grade.html',context)
    
def grades(request,pk):
    if not request.user.is_authenticated:
        return redirect("login")
    else:
        subjects = Subject.objects.all()
        class_schedules = Class_Schedule.objects.get(id=pk)
        subject_taken = SubjectTaken.objects.all()
        faculty = Faculty_user.objects.get(id=request.user.id)
        enrollment_detail = EnrollmentDetail.objects.all()
        context = {
              'parent':'',
              'segment':'grade',
              'subject_taken':subject_taken,   
              'faculty':faculty,
              'enrollment_detail':enrollment_detail, 
              'class_schedules':class_schedules, 
              'subjects':subjects, 
        } 
        return render(request, 'faculty/grades/grades.html',context)

def edit_grade(request,pk):
    subject_taken = get_object_or_404(SubjectTaken, pk=pk)
    if(request.method == 'POST'):
            form = FacultyGradeForm(request.POST, instance=subject_taken)
    else:    
            form = FacultyGradeForm(instance=subject_taken)
    return save_grade(request, form, 'faculty/grades/edit_grade.html')


def save_grade(request, form, template_name):
    data = dict()
    if form.is_valid():
        form.save()
        data['form_is_valid'] = True
        subjects = Subject.objects.all()
        subject_taken = SubjectTaken.objects.all()
        faculty = Faculty_user.objects.get(id=request.user.id)
        enrollment_detail = EnrollmentDetail.objects.all()
        data['grade_list'] = render_to_string('faculty/grades/grade_list.html',{'subject_taken':subject_taken,'faculty':faculty,'enrollment_detail':enrollment_detail,'subjects':subjects, })
    else:
        data['form_is_valid'] = False

    context = {'form':form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)
    
    
def grades_report(request,pk):
    subjects = Subject.objects.all()
    class_schedules = Class_Schedule.objects.get(id=pk)
    subject_taken = SubjectTaken.objects.all()
    faculty = Faculty_user.objects.get(id=request.user.id)
    enrollment_detail = EnrollmentDetail.objects.all()
    context = {
            'parent':'',
            'segment':'grade',
            'subject_taken':subject_taken,   
            'faculty':faculty,
            'enrollment_detail':enrollment_detail, 
            'class_schedules':class_schedules, 
            'subjects':subjects, 
    } 
    html = get_template('faculty/grades/grades_report.html').render(context)


    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'

    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

#/////////////////////////////////////////
# class schedule
#////////////////////////////////////////

def faculty_class_schedule_list(request):
    if not request.user.is_authenticated:
        return redirect("login")
    else:
        enrollment = Enrollment.objects.all()
        context = {
              'parent':'',
              'segment':'class-schedule',
              'enrollment':enrollment,     
        }
        return render(request, 'faculty/class_schedule/enrollment_class_schedule.html',context)

def faculty_class_schedules(request,pk):
    if not request.user.is_authenticated:
        return redirect("login")
    else:
        course = Course.objects.all()
        subjects = Subject.objects.all()
        class_schedules = Class_Schedule.objects.all()
        subject_taken = SubjectTaken.objects.all()
        enrollment = Enrollment.objects.get(id=pk)
        faculty = Faculty_user.objects.get(id=request.user.id)
        enrollment_detail = EnrollmentDetail.objects.all()
        context = {
              'parent':'',
              'segment':'class-schedule',
              'subject_taken':subject_taken,   
              'faculty':faculty,
              'enrollment':enrollment,
              'enrollment_detail':enrollment_detail, 
              'class_schedules':class_schedules,  
              'subjects':subjects,
              'course':course,
        }  
        return render(request, 'faculty/class_schedule/class_schedule.html',context)
    
def schedule_student_list(request,pk):
    if not request.user.is_authenticated:
        return redirect("login")
    else:
        class_schedules = Class_Schedule.objects.get(id=pk)
        subject_taken = SubjectTaken.objects.all()
        faculty = Faculty_user.objects.get(id=request.user.id)
        enrollment_detail = EnrollmentDetail.objects.all()
        context = {
              'parent':'',
              'segment':'class-schedule',
              'subject_taken':subject_taken,   
              'faculty':faculty,
              'enrollment_detail':enrollment_detail, 
              'class_schedules':class_schedules,  
        }  
        return render(request, 'faculty/class_schedule/schedule_student_list.html',context)
    
    
def faculty_class_schedule_report(request,pk):
    course = Course.objects.all()
    subjects = Subject.objects.all()
    class_schedules = Class_Schedule.objects.all()
    subject_taken = SubjectTaken.objects.all()
    enrollment = Enrollment.objects.get(id=pk)
    faculty = Faculty_user.objects.get(id=request.user.id)
    enrollment_detail = EnrollmentDetail.objects.all()
    context = {
            'parent':'',
            'segment':'class-schedule',
            'subject_taken':subject_taken,   
            'faculty':faculty,
            'enrollment':enrollment,
            'enrollment_detail':enrollment_detail, 
            'class_schedules':class_schedules,  
            'subjects':subjects,
            'course':course,
    } 

    html = get_template('faculty/class_schedule/class_schedule_report.html').render(context)


    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'

    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


def class_schedule_student_list_report(request,pk):
    class_schedules = Class_Schedule.objects.get(id=pk)
    subject_taken = SubjectTaken.objects.all()
    faculty = Faculty_user.objects.get(id=request.user.id)
    enrollment_detail = EnrollmentDetail.objects.all()
    context = {
            'parent':'',
            'segment':'class-schedule',
            'subject_taken':subject_taken,   
            'faculty':faculty,
            'enrollment_detail':enrollment_detail, 
            'class_schedules':class_schedules,  
    }   

    html = get_template('faculty/class_schedule/student_list_report.html').render(context)


    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'

    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response