from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm

def register(request):
    if request.method == "POST":
        # POST request
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # Save user
            form.save()

            # Feedback

            # For front-end render
            username = form.cleaned_data.get("username")
            messages.success(request, f"Account created for {username}!")

            # Return front end
            return redirect("blog-home")

    else:
        # GET request
        form = UserRegisterForm()
    return render(request, "users/register.html", {"form": form})
