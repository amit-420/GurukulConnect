from django.db import models
from datetime import datetime
from django.utils import timezone

class TutorialCategory(models.Model):

    tutorial_category = models.CharField(max_length=200)
    category_summary = models.CharField(max_length=200)
    category_slug = models.CharField(max_length=200, default=1)

    class Meta:
        # Gives the proper plural name for admin
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.tutorial_category

class TutorialSeries(models.Model):
    tutorial_series = models.CharField(max_length=200)
    tutorial_category = models.ForeignKey(TutorialCategory, default=1, verbose_name="Category", on_delete=models.SET_DEFAULT)
    series_summary = models.CharField(max_length=200)

    class Meta:
        # otherwise we get "Tutorial Seriess in admin"
        verbose_name_plural = "Series"

    def __str__(self):
        return self.tutorial_series

# Create your models here.py
class Tutorial(models.Model):
    tutorial_title = models.CharField(max_length=200)
    tutorial_content = models.TextField()
    tutorial_published = models.DateTimeField('date published')
    tutorial_series = models.ForeignKey(TutorialSeries, default=1, verbose_name="Series", on_delete=models.SET_DEFAULT)
    tutorial_slug = models.CharField(max_length=200, default=1)
    def __str__(self):
        return self.tutorial_title
# class MyModel(models.Model): 
  
#     # file will be uploaded to MEDIA_ROOT / uploads 
#     upload = models.ImageField(upload_to ='templates/assets/images/') 

class Notice(models.Model):
    notice_title = models.CharField(max_length=200)
    notice_published = models.DateTimeField('date published')
    notice_content = models.TextField()
    def __str__(self):
        return self.notice_title

class downlink(models.Model):
    downlink_title = models.CharField(max_length=200)
    downlink_published = models.DateTimeField('date published')
    downlink_slug = models.CharField(max_length=200,default=1)
    def __str__(self):
        return self.downlink_title

class EducatorsData(models.Model):
    educators_title = models.CharField( max_length=200)
    educators_email = models.EmailField(max_length=254)
    educators_no = models.CharField( max_length=10)
    def __str__(self):
        return self.educators_no
    class Meta:
        db_table = "educatorsData"