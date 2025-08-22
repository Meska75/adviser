from django.urls import path
from AIadviser.views import *

app_name = 'aiadviser'

urlpatterns = [
    path('', questions_view , name= 'questions'),
    path('result/', airesult , name= 'airesult'),
]