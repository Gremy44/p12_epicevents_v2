from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Client
    
class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client
    template_name = 'customer_management/customer_detail.html'
    context_object_name = 'customer'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        customer = self.get_object()  # Récupère l'objet Contract pour accéder à ses attributs
        context['customer'] = customer
        return context
    
class ClientListView(LoginRequiredMixin, ListView):
    model = Client
    template_name = 'customer_management/customer_tab.html'
    context_object_name = 'customers'
    
class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    template_name = 'customer_management/customer_add_update_form.html'
    fields = ['complete_name', 'email', 'phone', 'company_name', 'sale_contact']
    
    def get_success_url(self):
        return reverse_lazy('customers')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['add_or_update'] = False
        return context
    

class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    template_name = 'customer_management/customer_add_update_form.html'
    fields = ['complete_name', 'email', 'phone', 'company_name', 'sale_contact']
    
    def get_success_url(self):
        return reverse_lazy('customers')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['add_or_update'] = True
        return context
    
class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    template_name = 'customer_management/customer_delete_form.html'
    success_url = '/customers/'
    