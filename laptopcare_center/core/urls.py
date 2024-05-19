# core/urls.py
from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('services/', views.service, name='service'),
    path('contact/', views.contact, name='contact'),
    path('contact/success/', views.success, name='success'),
    path('footer-contact/', views.footer_contact, name='footer_contact'),
    path('test-footer-contact/', views.test_footer_contact, name='test_footer_contact'),
]