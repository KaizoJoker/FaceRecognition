from django.db import models
from django.db.models import Model
from sqlalchemy import true


class Lecturer (Model):
    className = models.CharField(max_length=70)
    lecturerName=models.CharField(max_length=70)
    time = models.DateTimeField()

    def __str__(self):
        return self.className+ '  ' + self.lecturerName

types = [('Student','Student'),('Lecturer','Lecturer')]
class Profile(models.Model):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    date = models.DateField()
    phone = models.BigIntegerField()
    email = models.EmailField()
    matricNo = models.CharField(max_length=200)
    status = models.CharField(choices=types,max_length=20,null=True,blank=False,default='Student')
    present = models.BooleanField(default=False)
    image = models.ImageField()
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.first_name +' '+self.last_name


class LastFace(models.Model):
    last_face = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.last_face


