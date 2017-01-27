from django.shortcuts import render
from .models import Contact
from .forms import ContactForm
from django.contrib import messages

def contact_form(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)

        instance.save()
        messages.success(request, "Successfully Created")
    context = {
        "form": form
    }
    return render(request, "contact/contact_form.html",context)
