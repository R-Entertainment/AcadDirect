from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse, HttpResponseRedirect, Http404
from . models import Student, Faculty, Document
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.core.paginator import Paginator


# Create your views here.
def manageStudents(request):
    student_list = Student.objects.all().order_by('-date_created')
    paginator = Paginator(student_list, 5)

    page_number = request.GET.get('page')
    student_list = paginator.get_page(page_number) 

    return render(request, 'admin/manageStudents.html', {'studentPage_object': student_list})

def addStudent(request):
    return render(request, 'admin/addStudent.html')

def processAddStudent(request):
    student_fname = request.POST.get('student_fname')
    student_lname = request.POST.get('student_lname')
    student_email = request.POST.get('student_email')
    student_password = request.POST.get('student_password')
    student_department = request.POST.get('student_department')
    try:
        n = Student.objects.get(student_email=student_email)
        return render(request, 'admin/addStudent.html', {
        'error_message' : 'Student with email %s already exists' % student_email
    })
    except ObjectDoesNotExist:
        student = Student.objects.create(student_email=student_email, student_fname=student_fname, student_lname=student_lname, student_password=student_password, student_department=student_department)
        student.save()
        return HttpResponseRedirect('/system-admin/manage-students')

def studentDetails(request, student_id):
    try:
        student = Student.objects.get(pk=student_id)
    except Student.DoesNotExist:
        raise Http404("Student does not Exist!")
    return render(request, 'admin/studentDetails.html', {'student': student})

def studentDelete(request, student_id):
    Student.objects.filter(id=student_id).delete()
    return HttpResponseRedirect('/system-admin/manage-students')

def editStudent(request, student_id):
    try:
        student = Student.objects.get(pk=student_id)
    except Student.DoesNotExist:
        raise Http404("Student does not Exist!")
    return render(request, 'admin/editStudent.html', {'student': student})

def processEditStudent(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    try:
            student_fname = request.POST.get('student_fname')
            student_lname = request.POST.get('student_lname')
            student_email = request.POST.get('student_email')
            student_password = request.POST.get('student_password')
            student_department = request.POST.get('student_department')
    except(KeyError, Student.DoesNotExist):
        return render(request, 'admin/studentDetails.html',
            {
            'student':student,
            'error_message': "There was an issue upon updating this student",
        })
    else:
        student_profile = Student.objects.get(id=student_id)
        student_profile.student_fname = student_fname
        student_profile.student_lname = student_lname
        student_profile.student_email = student_email
        student_profile.student_password = student_password
        student_profile.student_department = student_department
        student_profile.save()
        return HttpResponseRedirect(reverse('systemAdmin:studentDetails', args=(student_id, )))





def manageFaculties(request):
    faculty_list = Faculty.objects.order_by('-date_created')[:10]
    context = {'faculty_list' : faculty_list}
    return render(request, 'admin/manageFaculties.html', context)

def addFaculty(request):
    return render(request, 'admin/addFaculty.html')

def processAddFaculty(request):
    faculty_fname = request.POST.get('faculty_fname')
    faculty_lname = request.POST.get('faculty_lname')
    faculty_email = request.POST.get('faculty_email')
    faculty_password = request.POST.get('faculty_password')
    faculty_department = request.POST.get('faculty_department')
    try:
        n = Faculty.objects.get(faculty_email=faculty_email)
        return render(request, 'admin/addFaculty.html', {
        'error_message' : 'Faculty with email %s already exists' % faculty_email
    })
    except ObjectDoesNotExist:
        faculty = Faculty.objects.create(faculty_email=faculty_email, faculty_fname=faculty_fname, faculty_lname=faculty_lname, faculty_password=faculty_password, faculty_department=faculty_department)
        faculty.save()
        return HttpResponseRedirect('/system-admin/manage-faculties')

def facultyDetails(request, faculty_id):
    try:
        faculty = Faculty.objects.get(pk=faculty_id)
    except Faculty.DoesNotExist:
        raise Http404("Faculty does not Exist!")
    return render(request, 'admin/facultyDetails.html', {'faculty': faculty})

def facultyDelete(request, faculty_id):
    Faculty.objects.filter(id=faculty_id).delete()
    return HttpResponseRedirect('/system-admin/manage-faculties')

def editFaculty(request, faculty_id):
    try:
        faculty = Faculty.objects.get(pk=faculty_id)
    except Faculty.DoesNotExist:
        raise Http404("Faculty does not Exist!")
    return render(request, 'admin/editFaculty.html', {'faculty': faculty})

def processEditFaculty(request, faculty_id):
    faculty = get_object_or_404(Faculty, pk=faculty_id)
    try:
            faculty_fname = request.POST.get('faculty_fname')
            faculty_lname = request.POST.get('faculty_lname')
            faculty_email = request.POST.get('faculty_email')
            faculty_password = request.POST.get('faculty_password')
            faculty_department = request.POST.get('faculty_department')
    except(KeyError, Faculty.DoesNotExist):
        return render(request, 'admin/facultyDetails.html',
            {
            'faculty':faculty,
            'error_message': "There was an issue upon updating this faculty member.",
        })
    else:
        faculty_profile = Faculty.objects.get(id=faculty_id)
        faculty_profile.faculty_fname = faculty_fname
        faculty_profile.faculty_lname = faculty_lname
        faculty_profile.faculty_email = faculty_email
        faculty_profile.faculty_password = faculty_password
        faculty_profile.faculty_department = faculty_department
        faculty_profile.save()
        return HttpResponseRedirect(reverse('systemAdmin:facultyDetails', args=(faculty_id, )))





def manageDocuments(request):
    document_list = Document.objects.order_by('-date_created')[:10]
    context = {'document_list' : document_list}
    return render(request, 'admin/manageDocuments.html', context)

def addDocument(request):
    return render(request, 'admin/addDocument.html')

def processAddDocument(request):
    docu_title = request.POST.get('docu_title')
    docu_authors = request.POST.get('docu_authors')
    docu_published = request.POST.get('docu_published')
    docu_cover = request.FILES.get('docu_cover')
    docu_department = request.POST.get('docu_department')
    docu_topic = request.POST.get('docu_topic')
    docu_abstract = request.POST.get('docu_abstract')
    docu_file = request.FILES.get('docu_file')
    try:
        n = Document.objects.get(docu_title=docu_title)
        return render(request, 'admin/addDocument.html', {
        'error_message' : 'Document with title %s already exists' % docu_title
    })
    except ObjectDoesNotExist:
        document = Document.objects.create(docu_title=docu_title, docu_authors=docu_authors, docu_published=docu_published, docu_cover=docu_cover, docu_department=docu_department, docu_topic=docu_topic, docu_abstract=docu_abstract, docu_file=docu_file)
        document.save()
        return HttpResponseRedirect('/system-admin/manage-documents')

def documentDetails(request, docu_id):
    try:
        document = Document.objects.get(pk=docu_id)
    except Document.DoesNotExist:
        raise Http404("Document does not Exist!")
    return render(request, 'admin/documentDetails.html', {'document': document})

def documentDelete(request, docu_id):
    Document.objects.filter(id=docu_id).delete()
    return HttpResponseRedirect('/system-admin/manage-documents')

def editDocument(request, docu_id):
    try:
        document = Document.objects.get(pk=docu_id)
    except Document.DoesNotExist:
        raise Http404("Document does not Exist!")
    return render(request, 'admin/editDocument.html', {'document': document})

def processEditDocument(request, docu_id):
    document = get_object_or_404(Document, pk=docu_id)
    try:
        docu_title = request.POST.get('docu_title')
        docu_authors = request.POST.get('docu_authors')
        docu_published = request.POST.get('docu_published')
        docu_cover = request.FILES.get('docu_cover')
        docu_department = request.POST.get('docu_department')
        docu_topic = request.POST.get('docu_topic')
        docu_abstract = request.POST.get('docu_abstract')
        docu_file = request.FILES.get('docu_file')
    except(KeyError, Document.DoesNotExist):
        return render(request, 'admin/documentDetails.html',
            {
            'document':document,
            'error_message': "There was an issue upon updating this document.",
        })
    else:
        docu_profile = Document.objects.get(id=docu_id)
        docu_profile.docu_title = docu_title
        docu_profile.docu_authors = docu_authors
        docu_profile.docu_published = docu_published
        docu_profile.docu_cover = docu_cover
        docu_profile.docu_department = docu_department
        docu_profile.docu_topic = docu_topic
        docu_profile.docu_abstract = docu_abstract
        docu_profile.docu_file = docu_file
        docu_profile.save()
        return HttpResponseRedirect(reverse('systemAdmin:documentDetails', args=(docu_id, )))



def adminLogIn(request):
    return render(request, 'admin/adminLogIn.html')