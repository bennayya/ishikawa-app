from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# Define GENDER_CHOICES
GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),
]


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=100, blank=True)
    
    

    def __str__(self):
        return self.user.username
    
    class Meta:
        ordering = []
   