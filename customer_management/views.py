from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from .models import Client

from django.contrib.auth.decorators import permission_required, user_passes_test
from django.utils.decorators import method_decorator


class ClientDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Client
    template_name = 'customer_management/customer_detail.html'
    context_object_name = 'customer'
    permission_required = 'customer_management.view_client'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        customer = self.get_object()  # Récupère l'objet Client pour accéder à ses attributs
        context['customer'] = customer
        return context


class ClientListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    
    model = Client
    template_name = 'customer_management/customer_tab.html'
    context_object_name = 'customers'
    permission_required = 'customer_management.view_client'
    

class ClientCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Client
    template_name = 'customer_management/customer_add_update_form.html'
    fields = ['complete_name', 'email', 'phone', 'company_name', 'sale_contact']
    permission_required = 'customer_management.add_client'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['add_or_update'] = False
        return context
    

class ClientUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Client
    template_name = 'customer_management/customer_add_update_form.html'
    fields = ['complete_name', 'email', 'phone', 'company_name', 'sale_contact']
    permission_required = 'customer_management.change_client'
    
    def get_success_url(self):
        return reverse_lazy('customers')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['add_or_update'] = True
        return context


class ClientDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Client
    template_name = 'customer_management/customer_delete_form.html'
    success_url = '/customers/'
    permission_required = 'customer_management.delete_client'
    