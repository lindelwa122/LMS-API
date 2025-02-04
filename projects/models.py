from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False, unique=True)
    url = models.CharField(max_length=500, blank=False, null=False, unique=True)
    due_date = models.DateTimeField(blank=False, null=False)
