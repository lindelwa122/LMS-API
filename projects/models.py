from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False, unique=True)
    url = models.CharField(max_length=500, blank=False, null=False, unique=True)
    due_date = models.DateTimeField(blank=False, null=False)
    
    def __str__(self):
        return self.name


class Student(models.Model):
    username = models.CharField(max_length=100, blank=False, null=False, unique=True)
    
    def __str__(self):
        return self.username
    

class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='student')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project')
    score = models.FloatField()
    
    def __str__(self):
        return f'{self.student} ({self.project}) = {self.score}'
