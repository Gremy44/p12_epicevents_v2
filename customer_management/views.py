from django.shortcuts import render
from .models import Client

def get_costumer(request):
    customers = Client.objects.all()
    return render(request,
                  'customer_management/customer_tab.html',
                  context={'customers': customers},)