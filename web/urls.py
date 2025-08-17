from django.urls import path
from web.views import *

app_name = 'web'

urlpatterns = [
    path('', index_view, name = 'index'),
    path('services', service_view, name = 'services'),
    path('contact',contact_view , name = 'contact'),
    path('about', about_view , name = 'about'),
    path('policy', policy_view , name = 'policy'),
]