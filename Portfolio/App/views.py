from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact
from django.contrib import messages
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        message = request.POST.get('message')

        print(f"Name: {name}, Email: {email}, Number: {number}, Message: {message}")

        if name and email and number and message:
            Contact.objects.create(name=name, email=email, number=number, message=message)
            messages.success(request, 'Your message has been sent!')
        else:
            messages.error(request, 'Please fill all fields correctly.')

    return render(request, 'App/contact.html')