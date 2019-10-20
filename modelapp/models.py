from django.db import models

# Create your models here.
class Student(models.Model):
    sno=models.IntegerField()
    sname=models.CharField(max_length=60)
    scourse=models.CharField(max_length=60)
    smarks=models.IntegerField()

    def __str__(self):
        return self.sname
