
from __future__ import unicode_literals
from django.db import models
class report (models.Model):
    No = models.CharField(max_length=40,default="",editable=False)
    Title = models.CharField(max_length=40)
    Inventors = models.CharField(max_length=80)
    Applicants = models.CharField(max_length=40)
##Country = models.CharField(max_length=40)
    IPC = models.CharField(max_length=480)
    CPC = models.CharField(max_length=480)
    Country = models.CharField(max_length=50, default="", editable=False)
    Publication_number = models.CharField(max_length=40, default="", editable=False)
    Publication_date = models.CharField(max_length=10, default="", editable=False)
    Publication_Year = models.CharField(max_length=40,default="", editable=False)
    Earliest_publication = models.CharField(max_length=40,default="", editable=False)
    Family_number = models.CharField(max_length=80,default="", editable=False)
    Earliest_priority = models.CharField(max_length=80,default="",editable=False)
