from django.shortcuts import render, redirect
from .forms import ContactForm


def contact_view(request):
    contact_form=ContactForm()
    if request.method == "POST":
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            return redirect('home')

    content={
    	"contact_form": contact_form
    }
    return render(request, 'contact.html', content)
