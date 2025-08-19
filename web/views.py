from django.shortcuts import render , redirect
from web.forms import ContactForm
from django.contrib import messages


# Create your views here.

def index_view(request):
    return render(request , 'website/index.html')

def service_view(request):
    return render(request , 'website/services.html')

def about_view(request):
    return render(request , 'website/about.html')

from django.contrib import messages
from django.shortcuts import render
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            edied_form = form.save(commit=False)
            edied_form.save()
            messages.success(request, "your message sended successfully")
            form = ContactForm()  # فرم خالی بعد از ذخیره
        else:
            messages.error(request, "your message failded!")
    else:
        form = ContactForm()
    return render(request, 'website/contact.html', {'form': form})


def policy_view(request):
    return render(request , 'website/policy.html')