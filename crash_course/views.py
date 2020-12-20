from django.shortcuts import render
from django.views import View
from crash_course.models import CrashCourse, CourseChapter, ChapterSection
from django.http import JsonResponse
from .serializers import CrashCourseSerializer, CourseChapterSerializer
# Create your views here.

class CrashCourseList(View):
    def get(self, request):
        queryset = CrashCourse.objects.all()
        serializer_data = CrashCourseSerializer(queryset, many=True).data
        return JsonResponse({'crash_course': serializer_data})


class CourseChapterList(View):
    def get(self, request, course_slug):
        queryset = CourseChapter.objects.filter(course__slug=course_slug)
        serializer_data = CourseChapterSerializer(queryset, many=True).data
        return JsonResponse({'course_chapter': serializer_data})


class ChapterSectionList(View):
    queryset = ChapterSection.objects.all()
    context_object_name = 'chapter_section'


class SectionContentList(View):
    queryset = ChapterSection.objects.all()
    context_object_name = 'section_content'
