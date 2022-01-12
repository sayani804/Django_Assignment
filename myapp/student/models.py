from django.db import models

# Create your models here.

class StudentInfo(models.Model):
    rollNo = models.IntegerField(primary_key=True,  unique=True)
    name = models.CharField(max_length=255, null=False, blank=False )
    student_class = models.IntegerField(null=False, blank=False )
    school = models.CharField(max_length=255, null=False, blank=False)
    mobile = models.CharField(max_length=10, null=False, blank=False)
    address = models.CharField(max_length=255, null=True, blank=True)

class StudentAcademics(models.Model):
    rollNo = models.ForeignKey(StudentInfo, null=True, blank=True, on_delete=models.SET_NULL)
    maths = models.IntegerField( null=True, blank=True )
    physics = models.IntegerField( null=True, blank=True )
    chemistry = models.IntegerField( null=True, blank=True )
    biology = models.IntegerField( null=True, blank=True )
    english = models.IntegerField( null=True, blank=True )
    