from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact

def index(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        contact = Contact(name=name, email=email, subject=subject, message=message)
        contact.save()
        messages.success(request, "Your message has been sent successfully!")
        return redirect("index")

    return render(request, "index.html")
