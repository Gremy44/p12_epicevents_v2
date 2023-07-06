from django.contrib import admin
from .models import Event, Contract

class EventAdmin(admin.ModelAdmin):
    list_display = ('event_name', 'client', 'contract', 'date_start', 'date_end', 'support_contact', 'location', 'attentees', 'notes')
    list_filter = ('client', 'contract', 'support_contact', 'location')
    search_fields = ('event_name', 'client', 'contract', 'date_start', 'date_end', 'support_contact', 'location', 'attentees', 'notes')
    
class ContractAdmin(admin.ModelAdmin):
    list_display = ('client', 'sale_contact', 'amount', 'rest', 'creation_date', 'status')
    list_filter = ('client', 'sale_contact', 'status')
    search_fields = ('client', 'sale_contact', 'amount', 'rest', 'creation_date', 'status')
    
register = admin.site.register(Event, EventAdmin)
register = admin.site.register(Contract, ContractAdmin)