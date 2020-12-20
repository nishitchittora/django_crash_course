from django.urls import path
from crash_course import views

urlpatterns = [
    path('courses', views.CrashCourseList),
]
