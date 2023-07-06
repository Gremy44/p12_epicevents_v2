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
                                   get_staff,
                                   update_staff,)

from customer_management.views import get_costumer

from events_management.views import (get_events,
                                     get_contracts,)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_page, name='login'),
    path('logout/', logout_user, name='logout'),
    path('home/', home, name='home'),
    path('customers/', get_costumer, name='customers'),
    path('events/', get_events, name='events' ),
    path('contracts/', get_contracts, name='contracts' ),
    path('staff/', get_staff, name='staff'),
    path('staff/update/<int:user_id>/', update_staff, name='update_staff'),

]
