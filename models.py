from django.db import models
from datetime import datetime
from django.utils import timezone
import os, random
from django.utils.html import mark_safe


# Create your models here. 
now = timezone.now()

def document_path(instance, filename):
    basefilename, file_extension = os.path.splitext(filename)
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    randomstr = ''.join((random.choice(chars)) for x in range(10))
    _now = datetime.now()

    return 'uploads/{year}-{month}-{fileid}-{basename}-{randomstring}{ext}'.format(fileid = instance, basename=basefilename, randomstring=randomstr, ext=file_extension, year=now.strftime('%Y'), month=_now.strftime('%m'), day=_now.strftime('%d'))

def cover_path(instance, filename):
    basefilename, file_extension = os.path.splitext(filename)
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    randomstr = ''.join((random.choice(chars)) for x in range(10))
    _now = datetime.now()

    return 'uploads/docuCovers/{year}-{month}-{fileid}-{basename}-{randomstring}{ext}'.format(fileid = instance, basename=basefilename, randomstring=randomstr, ext=file_extension, year=now.strftime('%Y'), month=_now.strftime('%m'), day=_now.strftime('%d'))

class Student(models.Model):
    class Departments(models.TextChoices):
        CIVIL_ENGINEERING = 'CE', 'Civil Engineering'
        ELECTRICAL_ENGINEERING = 'EE', 'Electrical Engineering'
        INFORMATION_TECHNOLOGY = 'IT', 'Information Technology'

    student_fname = models.CharField(max_length=200, default='First Name', verbose_name='First Name', blank=False)
    student_lname = models.CharField(max_length=200, default='Last Name', verbose_name='Last Name', blank=False)
    student_email = models.EmailField(unique=True, max_length=200, default='Institutional Email', verbose_name='Student Email', blank=False)
    student_password = models.CharField(max_length=7, default='Password', verbose_name='Password', blank=False)
    student_department = models.CharField(max_length=200, choices=(Departments.choices), verbose_name='Department', blank=False)
    date_created = models.DateTimeField(default=now)
    
    def __str__(self):
        return self.student_email

class Faculty(models.Model):
    class Departments(models.TextChoices):
        CIVIL_ENGINEERING = 'CE', 'Civil Engineering'
        ELECTRICAL_ENGINEERING = 'EE', 'Electrical Engineering'
        INFORMATION_TECHNOLOGY = 'IT', 'Information Technology'

    faculty_fname = models.CharField(max_length=200, default='First Name', verbose_name='First Name', blank=False)
    faculty_lname = models.CharField(max_length=200, default='Last Name', verbose_name='Last Name', blank=False)
    faculty_email = models.EmailField(unique=True, max_length=200, default='Email', verbose_name='Email', blank=False)
    faculty_password = models.CharField(max_length=200, default='Password', verbose_name='Password', blank=False)
    faculty_department = models.CharField(max_length=200, choices=(Departments.choices), verbose_name='Department', blank=False)
    date_created = models.DateTimeField(default=now)

    def __str__(self):
        return self.faculty_email

# class DocuAuthor(models.Model):
#     docu_author_fname = models.CharField(max_length=200, default='First Name', verbose_name='First Name')
#     docu_author_lname = models.CharField(max_length=200, default='Last Name', verbose_name='Last Name')

class Document(models.Model):
    class Departments(models.TextChoices):
        CIVIL_ENGINEERING = 'CE', 'Civil Engineering'
        ELECTRICAL_ENGINEERING = 'EE', 'Electrical Engineering'
        INFORMATION_TECHNOLOGY = 'IT', 'Information Technology'

    docu_title = models.CharField(unique=True, max_length=200, default='Document Title', verbose_name='Title', blank=False)
    docu_authors = models.CharField(max_length=900, default='Document Author/s', verbose_name='Author/s', blank=False)
    docu_published = models.DateField(default=now, verbose_name='Published Date', blank=False)
    docu_cover = models.ImageField(upload_to=cover_path, blank=False)
    docu_department = models.CharField(max_length=200, choices=(Departments.choices), verbose_name='Department', blank=False)
    docu_topic = models.CharField(max_length=200, default='Document Topic', verbose_name='Document Topic', blank=False)
    docu_abstract = models.TextField(default='Document Abstract', verbose_name='Abstract', blank=False)
    docu_file = models.FileField(upload_to=document_path, verbose_name='Document File', blank=False)
    date_created = models.DateTimeField(default=now)
    
    def image_tag(self):
        return mark_safe ('<img src="/users/media/%s" width="50" height="50" />' % (self.docu_cover))
