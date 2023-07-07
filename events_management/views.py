from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import Event, Contract

    
def get_contracts(request):
    contracts = Contract.objects.all()
    return render(request,
                  'contracts/contracts_tab.html',
                  context={'contracts': contracts},)
    

class ContractDetailView(DetailView):
    model = Contract
    template_name = 'contracts/contracts_details.html'
    context_object_name = 'contracts'
    

class ContractListView(ListView):
    model = Contract
    template_name = 'contracts/contracts_tab.html'
    context_object_name = 'contracts'
    paginate_by = 10
    

class ContractCreateView(CreateView):
    model = Contract
    template_name = 'contracts/contracts_add_update_form.html'
    fields = ['amount', 'rest', 'status', 'client', 'sale_contact']
    
    def get_success_url(self):
        return reverse_lazy('contracts')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["add_or_update"] = False
        return context


class ContractUpdateView(UpdateView):
    model = Contract
    template_name = 'contracts/contracts_add_update_form.html'
    fields = ['amount', 'rest', 'status', 'client', 'sale_contact']
    
    def get_success_url(self):
        return reverse_lazy('contracts')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["add_or_update"] = True
        return context


class ContractDeleteView(DeleteView):
    model = Contract
    template_name = 'contracts/contracts_delete.html'
    success_url = '/contracts'
    
    
class EventDetailView(DetailView):
    model = Event
    template_name = 'events_management/events_details.html'
    context_object_name = 'events'
    

class EventListView(ListView):
    model = Event
    template_name = 'events_management/events_tab.html'
    context_object_name = 'events'
    paginate_by = 10
    
class EventCreateView(CreateView):
    model = Event
    template_name = 'events_management/events_add_update_form.html'  # Spécifiez le modèle pour le rendu du formulaire
    fields = ['event_name', 'date_start', 'date_end', 'location', 'attentees', 'notes', 'client', 'contract', 'support_contact']
    
    def get_success_url(self) -> str:
        return reverse_lazy('events')  # Redirige vers la liste du personnel après la mise à jour réussie

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["add_or_update"] = False
        return context
    

class EventUpdateView(UpdateView):
    model = Event
    template_name = 'events_management/events_add_update_form.html'  # Spécifiez le modèle pour le rendu du formulaire
    fields = ['event_name', 'date_start', 'date_end', 'location', 'attentees', 'notes', 'client', 'contract', 'support_contact']
    
    def get_success_url(self) -> str:
        return reverse_lazy('events')  # Redirige vers la liste du personnel après la mise à jour réussie

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["add_or_update"] = True
        return context
    
    
class EventDeleteView(DeleteView):
    model = Event
    template_name = 'events_management/events_delete.html'
    success_url = '/events'