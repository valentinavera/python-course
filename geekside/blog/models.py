from django.db import models

# Create your models here.
class Post(models.Model):
  title = models.CharField(max_length=150) # varchar 150
  text = models.TextField() # long text

  def __str__(self):
    return self.title
