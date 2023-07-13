from custom_cms_auth.models import User
from django.db import models

class Client(models.Model):
    complete_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    company_name = models.CharField(max_length=100)
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    sale_contact = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.complete_name