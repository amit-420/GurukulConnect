from django.contrib import admin
from .models import Tutorial, TutorialSeries,TutorialCategory,Notice,downlink,EducatorsData
from tinymce.widgets import TinyMCE
from django.db import models


# Register your models here.


class TutorialAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Title/date", {'fields': ["tutorial_title", "tutorial_published"]}),
        ("URL", {'fields': ["tutorial_slug"]}),
        ("Series", {'fields': ["tutorial_series"]}),
        ("Content", {"fields": ["tutorial_content"]})
    ]
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 30})},
        }

class NoticeAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Title/date", {"fields": ["notice_title","notice_published"]}),
        ("Content", {"fields": ["notice_content"]}),
    )

class downlinkAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Title/date", {"fields": ["downlink_title","downlink_published"],}),
        ("URL", {'fields': ["downlink_slug"]}),
    )

class educatorsInfoAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Name", {"fields": ["educators_title"],}),
        ("Info", {"fields": ["educators_email","educators_no"]})
    )
       



admin.site.register(TutorialSeries)
admin.site.register(TutorialCategory)
admin.site.register(Tutorial,TutorialAdmin)
admin.site.register(Notice,NoticeAdmin)
admin.site.register(downlink,downlinkAdmin)
admin.site.register(EducatorsData,educatorsInfoAdmin)