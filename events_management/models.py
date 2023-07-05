from customer_management.models import Client
from custom_cms_auth.models import User
from django.db import models

class Event(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    contract = models.ForeignKey('Contract' , on_delete=models.CASCADE)
    event_name = models.CharField(max_length=50)
    date_start = models.DateField()
    date_end = models.DateField()
    support_contact = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=125)
    attentees = models.IntegerField()
    notes = models.TextField()
    
class Contract(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    sale_contact = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    rest = models.DecimalField(max_digits=10, decimal_places=2)
    creation_date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    