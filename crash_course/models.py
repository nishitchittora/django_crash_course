from django.db import models
from .mixins import StatusMixin, TimeStampedModel, ImageMixin

# Create your models here.


class CrashCourse(TimeStampedModel, StatusMixin):
    title = models.CharField(max_length=128, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class CourseChapter(TimeStampedModel, StatusMixin):
    title = models.CharField(max_length=128, blank=True, null=True)
    description =  models.TextField(blank=True, null=True)
    course = models.Foreignkey(CrashCourse, null=True, blank=True)

    def __str__(self):
        return self.title


class ChapterSection(TimeStampedModel, StatusMixin):
    title = models.CharField(max_length=128, blank=True, null=True)
    description =  models.TextField(blank=True, null=True)
    chapter = models.Foreignkey(CourseChapter, null=True, blank=True)

    def __str__(self):
        return self.title


class SectionContent(TimeStampedModel, StatusMixin):
    title = models.CharField(max_length=128, blank=True, null=True)
    description =  models.TextField(blank=True, null=True)
    section = models.Foreignkey(ChapterSection, null=True, blank=True)

    def __str__(self):
        return self.title
