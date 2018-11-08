from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=254, blank=False)
    email = models.EmailField(max_length=254,blank=False)
    
    def __str__(self):
        return self.name
