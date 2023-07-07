from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Client
    
class ClientDetailView(DetailView):
    model = Client
    template_name = 'customer_management/customer_detail.html'
    context_object_name = 'customer'
    
class ClientListView(ListView):
    model = Client
    template_name = 'customer_management/customer_tab.html'
    context_object_name = 'customers'
    
class ClientCreateView(CreateView):
    model = Client
    template_name = 'customer_management/customer_add_update_form.html'
    fields = ['complete_name', 'email', 'phone', 'company_name', 'sale_contact']
    
    def get_success_url(self):
        return reverse_lazy('customers')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['add_or_update'] = False
        return context
    

class ClientUpdateView(UpdateView):
    model = Client
    template_name = 'customer_management/customer_add_update_form.html'
    fields = ['complete_name', 'email', 'phone', 'company_name', 'sale_contact']
    
    def get_success_url(self):
        return reverse_lazy('customers')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['add_or_update'] = True
        return context
    
class ClientDeleteView(DeleteView):
    model = Client
    template_name = 'customer_management/customer_delete_form.html'
    success_url = '/customers/'
    