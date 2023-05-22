from django.urls import path
from django.conf import settings
from . import views
from django.conf.urls.static import static

app_name = 'systemAdmin'
urlpatterns = [
    path('', views.adminLogIn, name='adminLogIn'),

    path('manage-students/', views.manageStudents, name='manageStudents'),
    path('add-student/', views.addStudent, name='addStudent'),
    path('processAddStudent', views.processAddStudent, name='processAddStudent'),
    path('<int:student_id>/student-details', views.studentDetails, name='studentDetails'),
    path('<int:student_id>/delete-student', views.studentDelete, name='studentDelete'),
    path('<int:student_id>/edit-student', views.editStudent, name='editStudent'),

    path('manage-faculties/', views.manageFaculties, name='manageFaculties'),
    path('add-faculty/', views.addFaculty, name='addFaculty'),
    path('processAddFaculty', views.processAddFaculty, name='processAddFaculty'),
    path('<int:faculty_id>/faculty-details', views.facultyDetails, name='facultyDetails'),
    path('<int:faculty_id>/delete-faculty', views.facultyDelete, name='facultyDelete'),
    path('<int:faculty_id>/edit-faculty', views.editFaculty, name='editFaculty'),

    path('manage-documents/', views.manageDocuments, name='manageDocuments'),
    path('add-document/', views.addDocument, name='addDocument'),
    path('processAddDocument', views.processAddDocument, name='processAddDocument'),
    path('<int:docu_id>/document-details', views.documentDetails, name='documentDetails'),
    path('<int:docu_id>/delete-document', views.documentDelete, name='documentDelete'),
    path('<int:docu_id>/edit-document', views.editDocument, name='editDocument'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)