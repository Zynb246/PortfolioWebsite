from django.db import models
from django.db.models.fields import AutoField

# Create your models here.

class Skill (models.Model):
    sno = models.AutoField(primary_key=True)
    skill_name = models.CharField(max_length=50, verbose_name="Skill Name")
    percent = models.CharField(max_length=4, verbose_name="Percent")
    
    def __str__(self):
         return self.skill_name + " - " + self.percent