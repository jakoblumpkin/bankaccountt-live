from django.shortcuts import render, redirect
from .forms import RegisterForm
from user.models import account
# Create your views here.
def register(request):
    if request.method=="POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST['username']
            account.objects.create(username=username, balance=0.0)
            redirect("/")
    else:
        form = RegisterForm()
    return render(request, "register/register.html", {"form":form})