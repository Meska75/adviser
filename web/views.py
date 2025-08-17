from django.shortcuts import render

# Create your views here.

def index_view(request):
    return render(request , 'website/index.html')

def service_view(request):
    return render(request , 'website/services.html')

def about_view(request):
    return render(request , 'website/about.html')

def contact_view(request):
    return render(request , 'website/contact.html')

def policy_view(request):
    return render(request , 'website/policy.html')