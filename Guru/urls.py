"""
Definition of urls for SpecialOrders.
"""

from datetime import datetime
from django.conf.urls import patterns, url
from specialOrders.forms import BootstrapAuthenticationForm

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^ind$','specialOrders.views.index',name='indexerino'),
    url(r'^$', 'specialOrders.views.home', name='home'),
    url(r'^contact$', 'specialOrders.views.contact', name='contact'),
    url(r'^about', 'specialOrders.views.about', name='about'),
    url(r'^orders$', 'specialOrders.views.orders', name='orders'),
    url(r'^orders/(?P<order_id>[0-9]+)/$', 'specialOrders.views.order_detail', name='detail'),
    url(r'^itemupdate', 'specialOrders.views.itemupdate', name='itemupdate'),
    url(r'^items', 'specialOrders.views.item_manager', name='items'),
    url(r'^admin/', include(admin.site.urls), name='admin'),
    url(r'^neworder', 'specialOrders.views.new_order_entry', name='neworder'),
    url(r'^login/$',
        'django.contrib.auth.views.login',
        {
            'template_name': 'app/login.html',
            'authentication_form': BootstrapAuthenticationForm,
            'extra_context':
            {
                'title':'Log in',
                'year':datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        'django.contrib.auth.views.logout',
        {
            'next_page': '/',
        },
        name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),




)

