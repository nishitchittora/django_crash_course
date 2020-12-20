from django.shortcuts import render
from django.views.generic import ListView, DetailView
from crash_course.models import CrashCourse, CourseChapter, ChapterSection, SectionContent

# Create your views here.

class CrashCourseList(ListView):
    queryset = CrashCourse.objects.all()
    context_object_name = 'crash_course'
