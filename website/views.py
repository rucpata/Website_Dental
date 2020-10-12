from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def contact(request):
    if request.method == 'POST':
         #do stuff
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']


        # Send email
        send_mail(
            message_name,#temat
            message,#treść wiadomości
            message_email,#od kogo
            ['stefan.kicia@gmial.com'],#do kogo
            fail_silently=False,
            )

        return render(request, 'contact.html', {'message_name': message_name})
    else:
        #return the page
        return render(request, 'contact.html', {})

def about(request):
    return render(request, 'about.html', {})

def blogdetails(request):
    return render(request, 'blog-details.html', {})

def blog(request):
    return render(request, 'blog.html', {})


def pricing(request):
    return render(request, 'pricing.html', {})

def service(request):
    return render(request, 'service.html', {})