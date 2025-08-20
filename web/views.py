from django.shortcuts import render , redirect
from web.forms import ContactForm
from django.contrib import messages
from .forms import ContactForm

# Create your views here.

def index_view(request):
    return render(request , 'website/index.html')

def service_view(request):
    return render(request , 'website/services.html')

def about_view(request):
    return render(request , 'website/about.html')


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message successfully sended!")
            return redirect('web:contact')
        else:
            messages.error(request, "somthing is wrong, check fields and try again.")
    else:
        form = ContactForm()
    return render(request, 'website/contact.html', {'form': form})


def policy_view(request):
    return render(request , 'website/policy.html')