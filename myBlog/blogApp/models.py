from django.db import models
from django.forms import CharField

# Create your models here.
class Blog(models.Model):
  sno=models.AutoField(primary_key=True)
  title=models.CharField(max_length=200)
  content=models.TextField()
  short_desc=models.CharField(max_length=300, default="")
  slug=models.CharField(max_length=100)
  time=models.DateTimeField(auto_now_add=True)

  def __str__(self):
      return self.title

class Contact(models.Model):
  name=models.CharField(max_length=100)
  email=models.EmailField()
  phone=models.CharField(max_length=13)
  desc=models.TextField()
  time=models.DateTimeField(auto_now_add=True)

  def __str__(self):
      return f"{self.name}, {self.email}"
