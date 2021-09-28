from django.shortcuts import redirect, render
from . models import Contact
# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        c= Contact(name=name,email=email,subject=subject,message=message)
        c.save()
        redirect('home')
    return render(request, 'pages/contact.html')

    
        