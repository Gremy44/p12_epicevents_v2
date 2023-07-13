from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import Event, Contract
    

class ContractDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Contract
    template_name = 'contracts/contracts_detail.html'
    context_object_name = 'contracts'
    permission_required = 'events_management.view_contract'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        contract = self.get_object()  # Récupère l'objet Contract pour accéder à ses attributs
        context['contract'] = contract
        return context
    

class ContractListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Contract
    template_name = 'contracts/contracts_tab.html'
    context_object_name = 'contracts'
    paginate_by = 10
    permission_required = 'events_management.view_contract'
    

class ContractCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Contract
    template_name = 'contracts/contracts_add_update_form.html'
    fields = ['amount', 'rest', 'status', 'client', 'sale_contact']
    permission_required = 'events_management.add_contract'
    
    def get_success_url(self):
        return reverse_lazy('contracts')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["add_or_update"] = False
        return context


class ContractUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Contract
    template_name = 'contracts/contracts_add_update_form.html'
    fields = ['amount', 'rest', 'status', 'client', 'sale_contact']
    permission_required = 'events_management.change_contract'
    
    def get_success_url(self):
        return reverse_lazy('contracts')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["add_or_update"] = True
        return context


class ContractDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Contract
    template_name = 'contracts/contracts_delete.html'
    success_url = '/contracts'
    permission_required = 'events_management.delete_contract'
    
    
class EventDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Event
    template_name = 'events_management/events_detail.html'
    context_object_name = 'events'
    permission_required = 'events_management.view_event'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        events = self.get_object()  # Récupère l'objet Contract pour accéder à ses attributs
        context['events'] = events
        return context
    

class EventListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Event
    template_name = 'events_management/events_tab.html'
    context_object_name = 'events'
    paginate_by = 10
    permission_required = 'events_management.view_event'
    
class EventCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Event
    template_name = 'events_management/events_add_update_form.html'  # Spécifiez le modèle pour le rendu du formulaire
    fields = ['event_name', 'date_start', 'date_end', 'location', 'attentees', 'notes', 'client', 'contract', 'support_contact']
    permission_required = 'events_management.add_event'
    
    def get_success_url(self) -> str:
        return reverse_lazy('events')  # Redirige vers la liste du personnel après la mise à jour réussie

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["add_or_update"] = False
        return context
    

class EventUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Event
    template_name = 'events_management/events_add_update_form.html'  # Spécifiez le modèle pour le rendu du formulaire
    fields = ['event_name', 'date_start', 'date_end', 'location', 'attentees', 'notes', 'client', 'contract', 'support_contact']
    permission_required = 'events_management.change_event'
    
    def get_success_url(self) -> str:
        return reverse_lazy('events')  # Redirige vers la liste du personnel après la mise à jour réussie

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["add_or_update"] = True
        return context
    
    
class EventDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Event
    template_name = 'events_management/events_delete.html'
    success_url = '/events'
    permission_required = 'events_management.delete_event'