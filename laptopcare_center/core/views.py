from django.shortcuts import render, redirect
from product.models import Category, Product
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

def index(request):
    products = Product.objects.filter(is_sold=False)[:6]
    categories = Category.objects.all()
    return render(request, 'core/index.html', {
        'categories': categories,
        'products': products,
    })

def service(request):
    return render(request, 'core/service.html')

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            full_message = f"Message from {name} ({email}):\n\n{message}"
            send_mail(
                f"Contact Form Submission: {name}",
                full_message,
                settings.EMAIL_HOST_USER,
                [settings.EMAIL_HOST_USER],
                fail_silently=False,
            )
            return redirect('core:success')
    else:
        form = ContactForm()
    return render(request, 'core/contact.html', {'form': form})

def success(request):
    return render(request, 'core/success.html', {'message': 'Your contact form submission was successful!'})

def footer_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            full_message = f"Message from {name} ({email}):\n\n{message}"
            send_mail(
                f"Contact Form Submission: {name}",
                full_message,
                settings.EMAIL_HOST_USER,
                [settings.EMAIL_HOST_USER],
                fail_silently=False,
            )
            return redirect('core:success')
    else:
        form = ContactForm()
    return render(request, 'core/contact.html', {'form': form})

def test_footer_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            full_message = f"Message from {name} ({email}):\n\n{message}"
            send_mail(
                f"Contact Form Submission: {name}",
                full_message,
                settings.EMAIL_HOST_USER,
                [settings.EMAIL_HOST_USER],
                fail_silently=False,
            )
            return redirect('core:success')
    else:
        form = ContactForm()
    return render(request, 'core/test_footer_contact.html', {'form': form})

