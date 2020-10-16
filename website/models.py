from django.db import models

# Create your models here.
class Courses(models.Model):
    course_id = models.IntegerField()
    department = models.CharField(max_length=250)
    course_number = models.CharField(max_length=250)
    course_name = models.CharField(max_length=250)
    semester = models.CharField(max_length=250)
    sem_year = models.CharField(max_length=250)
    grade = models.CharField(max_length=250)


class PreRequisite(models.Model):
    course_id = models.IntegerField(max_length=100)
    prereq1 = models.IntegerField(max_length=100)
    prereq2 = models.IntegerField(max_length=100)






