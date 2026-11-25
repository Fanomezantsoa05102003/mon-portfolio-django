from django.shortcuts import render, redirect
from .forms import ContactMessageForm


def contact_create(request):
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ContactMessageForm()

    return render(request, 'contact/contact_form.html', {
        'form': form
    })
