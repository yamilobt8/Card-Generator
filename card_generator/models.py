from django.db import models

# Create your models here.
class Participant(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    insta_url = models.URLField()
    dance_category = models.CharField(max_length=100)
    age = models.IntegerField()
    phone_number = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    picutre_url = models.URLField()
    def __str__(self):
        return self.full_name