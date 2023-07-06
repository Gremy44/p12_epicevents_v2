from django.contrib import admin
from .models import Client

class ClientAdmin(admin.ModelAdmin):
    list_display = ('complete_name', 'email', 'phone', 'company_name', 'sale_contact')
    list_filter = ('sale_contact',)
    search_fields = ('complete_name', 'email', 'phone', 'company_name')
    
register = admin.site.register(Client, ClientAdmin)
