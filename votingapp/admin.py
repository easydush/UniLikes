from django.contrib import admin
from votingapp.models import Teacher, Subject, CourseSubject, Rate

# Register your models here.
admin.site.register(Teacher)
admin.site.register(Subject)
admin.site.register(CourseSubject)
admin.site.register(Rate)
