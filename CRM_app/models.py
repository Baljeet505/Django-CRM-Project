from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Record(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    profile_image = models.ImageField(null=True,blank=True,upload_to='images/')


    def __str__(self):
        return f"{self.user.username}'s Record"