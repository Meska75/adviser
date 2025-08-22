from django.shortcuts import render , redirect
from web.forms import ContactForm
from django.contrib import messages
from .forms import ContactForm

import logging
from django.shortcuts import render
from django.http import JsonResponse

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


def custom_404(request, exception):
    # اگر می‌خواهید داده‌های اضافی ارسال کنید، اینجا اضافه کنید
    context = {
        "message": "صفحه مورد نظر پیدا نشد.",
        # "categories": Category.objects.all()  # مثال
    }
    return render(request, "404.html", context=context, status=404)

