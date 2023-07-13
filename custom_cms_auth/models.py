from django.contrib.auth.models import AbstractUser, Group, Permission, PermissionsMixin
from django.db import models
from django.contrib.auth.hashers import make_password

Group.objects.get_or_create(name='group_sale')
Group.objects.get_or_create(name='group_support')
Group.objects.get_or_create(name='group_gestion')

class User(AbstractUser, PermissionsMixin):
    
    role = models.ForeignKey('Role', on_delete=models.CASCADE, null=True, blank=True)
    
    def save(self, *args, **kwargs):
        if self.password:
            self.password = make_password(self.password)
        
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.username


class Role(models.Model):
    
    role = models.CharField(max_length=50)
    
    def __str__(self):
        return self.role