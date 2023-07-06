from django.shortcuts import render
from .models import Event, Contract

def get_events(request):
    events = Event.objects.all()
    return render(request,
                  'events_management/events_tab.html',
                  context={'events': events},)
    
def get_contracts(request):
    contracts = Contract.objects.all()
    return render(request,
                  'contracts/contracts_tab.html',
                  context={'contracts': contracts},)
