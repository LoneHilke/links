from django.db import models
from django.utils import timezone 
from django.conf import settings 

# Create your models here.
class Jango(models.Model):
  author = models.ForeignKey (settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  titel =  models.CharField (max_length = 
250)
  beskrivelse = models.CharField(max_length = 250)
  links = models.URLField ()
  created_date = models.DateTimeField(default=timezone.now)
  published_date = models.DateTimeField(blank=True, null=True)

  def publish(self):
        self.published_date = timezone.now()
        self.save()

  def __str__(self):
    return self.title 

