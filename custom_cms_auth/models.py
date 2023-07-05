from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    
    role = models.ForeignKey('Role', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.username


class Role(models.Model):
    
    role = models.CharField(max_length=50)
    
    def __str__(self):
        return self.role