from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username
    
class Notes(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    last_update = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
        
