from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import Event, Contract

    
def get_contracts(request):
    contracts = Contract.objects.all()
    return render(request,
                  'contracts/contracts_tab.html',
                  context={'contracts': contracts},)
    

class ContractDetailView(LoginRequiredMixin, DetailView):
    model = Contract
    template_name = 'contracts/contracts_detail.html'
    context_object_name = 'contracts'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        contract = self.get_object()  # Récupère l'objet Contract pour accéder à ses attributs
        context['contract'] = contract
        return context
    

class ContractListView(LoginRequiredMixin, ListView):
    model = Contract
    template_name = 'contracts/contracts_tab.html'
    context_object_name = 'contracts'
    paginate_by = 10
    

class ContractCreateView(LoginRequiredMixin, CreateView):
    model = Contract
    template_name = 'contracts/contracts_add_update_form.html'
    fields = ['amount', 'rest', 'status', 'client', 'sale_contact']
    
    def get_success_url(self):
        return reverse_lazy('contracts')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["add_or_update"] = False
        return context


class ContractUpdateView(LoginRequiredMixin, UpdateView):
    model = Contract
    template_name = 'contracts/contracts_add_update_form.html'
    fields = ['amount', 'rest', 'status', 'client', 'sale_contact']
    
    def get_success_url(self):
        return reverse_lazy('contracts')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["add_or_update"] = True
        return context


class ContractDeleteView(LoginRequiredMixin, DeleteView):
    model = Contract
    template_name = 'contracts/contracts_delete.html'
    success_url = '/contracts'
    
    
class EventDetailView(LoginRequiredMixin, DetailView):
    model = Event
    template_name = 'events_management/events_detail.html'
    context_object_name = 'events'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        events = self.get_object()  # Récupère l'objet Contract pour accéder à ses attributs
        context['events'] = events
        return context
    

class EventListView(LoginRequiredMixin, ListView):
    model = Event
    template_name = 'events_management/events_tab.html'
    context_object_name = 'events'
    paginate_by = 10
    
class EventCreateView(LoginRequiredMixin, CreateView):
    model = Event
    template_name = 'events_management/events_add_update_form.html'  # Spécifiez le modèle pour le rendu du formulaire
    fields = ['event_name', 'date_start', 'date_end', 'location', 'attentees', 'notes', 'client', 'contract', 'support_contact']
    
    def get_success_url(self) -> str:
        return reverse_lazy('events')  # Redirige vers la liste du personnel après la mise à jour réussie

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["add_or_update"] = False
        return context
    

class EventUpdateView(LoginRequiredMixin, UpdateView):
    model = Event
    template_name = 'events_management/events_add_update_form.html'  # Spécifiez le modèle pour le rendu du formulaire
    fields = ['event_name', 'date_start', 'date_end', 'location', 'attentees', 'notes', 'client', 'contract', 'support_contact']
    
    def get_success_url(self) -> str:
        return reverse_lazy('events')  # Redirige vers la liste du personnel après la mise à jour réussie

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["add_or_update"] = True
        return context
    
    
class EventDeleteView(LoginRequiredMixin, DeleteView):
    model = Event
    template_name = 'events_management/events_delete.html'
    success_url = '/events'