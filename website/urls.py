from django.urls import path
from .views import index, about, blogdetails, blog, contact, pricing, service

urlpatterns = [
    path('', index, name='index'),
    path('about.html', about, name='about'),
    path('blog-details.html', blogdetails, name='blogdetails'),
    path('blog.html', blog, name='blog'),
    path('contact.html', contact, name='contact'),
    path('pricing.html', pricing, name='pricing'),
    path('service.html', service, name='service'),
]
