from django.db import models
from django.contrib.auth.models import User
# Create your models here.
    

class UserNotes(models.Model):
    author = models.CharField(max_length=30)
    title = models.CharField(max_length=20)
    note = models.TextField()
    date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.title