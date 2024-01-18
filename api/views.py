from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Utilisateur

from .forms import LoginForm

user1 = 'jawhar'
password1 = 'moumen'

def login_view(request):
    form = LoginForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']

        # Check if the entered credentials match the predefined values
        if email == user1 and password == password1:
            # Credentials are correct, you can redirect or perform other actions here
            messages.success(request, 'Login successful!')
            return redirect('accueil')
        else:
            messages.error(request, 'Incorrect credentials. Please try again.')

    return render(request, 'login.html', {'form': form})
