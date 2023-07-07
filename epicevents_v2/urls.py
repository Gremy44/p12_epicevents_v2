"""epicevents_v2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from custom_cms_auth.views import (login_page, 
                                   logout_user,
                                   home,
                                   StaffListView,
                                   StaffCreateView,
                                   StaffDeleteView,
                                   StaffDetailView,
                                   StaffUpdateView,
                                   )

from customer_management.views import (ClientListView,
                                       ClientDetailView,
                                       ClientCreateView,
                                       ClientUpdateView,
                                       ClientDeleteView)

from events_management.views import (EventDetailView,
                                     EventListView,
                                     EventCreateView,
                                     EventUpdateView,
                                     EventDeleteView,
                                     ContractDetailView,
                                     ContractListView,
                                     ContractCreateView,
                                     ContractUpdateView,
                                     ContractDeleteView,)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_page, name='login'),
    path('logout/', logout_user, name='logout'),
    path('home/', home, name='home'),
    path('customers/', ClientListView.as_view(), name='customers'),
    path('customers/add/', ClientCreateView.as_view(), name='add_customers'),
    path('customers/update/<int:pk>/', ClientUpdateView.as_view(), name='update_customers'),
    path('customers/delete/<int:pk>/', ClientDeleteView.as_view(), name='delete_customers'),
    path('events/', EventListView.as_view(), name='events' ),
    path('events/add/', EventCreateView.as_view(), name='add_events' ),
    path('events/update/<int:pk>', EventUpdateView.as_view(), name='update_events' ),
    path('events/delete/<int:pk>', EventDeleteView.as_view(), name='delete_events' ),
    path('contracts/', ContractListView.as_view(), name='contracts' ),
    path('contracts/add/', ContractCreateView.as_view(), name='add_contracts' ),
    path('contracts/update/<int:pk>', ContractUpdateView.as_view(), name='update_contracts' ),
    path('contracts/delete/<int:pk>', ContractDeleteView.as_view(), name='delete_contracts' ),
    path('staff/', StaffListView.as_view() , name='staff'),
    path('staff/add/', StaffCreateView.as_view(), name='add_staff'),
    path('staff/update/<int:pk>/', StaffUpdateView.as_view(), name='update_staff'),
    path('staff/delete/<int:pk>/', StaffDeleteView.as_view(), name='delete_staff'),
]
