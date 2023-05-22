from django.contrib import admin
from .models import Student, Faculty, Document
from django.contrib.contenttypes.admin import GenericTabularInline

# Register your models here.

# admin.site.site_header = "AcadDirect System Admin"
# admin.site.site_title = "AcadDirect System Admin Log In"
# admin.site.index_title = "Welcome to the AcadDirect System Administration"

# class CommentInline(admin.TabularInline):
#     model = Comment
#     extra = 0

class SystemAdminSite(admin.AdminSite):
    site_header = 'AcadDirect System Admin'
    site_title = 'AcadDirect System Admin Log In'
    index_title = 'Welcome to the AcadDirect System Administration'

systemAdmin_site = SystemAdminSite(name='SystemAdmin')



class StudentAdmin(admin.ModelAdmin):
    list_display = ['student_fname', 'student_lname', 'student_email', 'student_password', 'student_department', 'date_created']
    search_fields = ['student_fname', 'student_lname', 'student_email', 'student_department']
    # inlines = [CommentInline]

class FacultyAdmin(admin.ModelAdmin):
    list_display = ['faculty_fname', 'faculty_lname', 'faculty_email', 'faculty_password', 'faculty_department', 'date_created']
    search_fields = ['student_fname', 'student_lname', 'faculty_email', 'faculty_department']

class DocuAdmin(admin.ModelAdmin):
    list_display = ['docu_title', 'docu_authors', 'docu_published', 'docu_cover','docu_department', 'docu_topic', 'docu_file', 'date_created']
    search_fields = ['docu_title', 'docu_authors', 'docu-published', 'docu_department', 'docu_topic']


# class CommentAdmin(admin.ModelAdmin):
#     list_display = ('name', 'body', 'user_id', 'created_on', 'active')
#     list_filter = ('active', 'created_on')
#     search_fields = ('name', 'email', 'body')
#     actions = ['approve_comment']

#     def approve_comment(self, request, queryset):
#         queryset.update(active=True)



systemAdmin_site.register(Student, StudentAdmin)
systemAdmin_site.register(Faculty, FacultyAdmin)
systemAdmin_site.register(Document, DocuAdmin)
# admin.site.register(Comment, CommentAdmin)