from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .extracode import *
from django.contrib.auth.models import User
# Create your views here.

def home(request):
    if request.user!='AnonymousUser':
        Accountbalance=finduser(request.user)
    if Accountbalance=='Created':
       Accountbalance=finduser(request.user)
    # Adds commas to number for display
    display=addcommas(float(("{:.2f}".format(Accountbalance))))

    context={"balance": display}
    return render(request, 'index.html', context)


def deposit(request):
    # if request.method == 'POST':
    #     addtodata(request.POST['title'], request.user)
    return render(request, 'deposit.html')


def depositmoney(request):
    if request.method == 'POST':
        addtodata(request.POST['title'], request.user)
    return redirect('/')


def withdraw(request):
    return render(request, 'withdraw.html')

def withdrawmoney(request):
    acc=account.objects.all()
    if request.method=='POST':
        for i in acc:
             if str(i.username)==str(request.user):
                subamount=0
                datanum=float(i.balance)
                subamount=float(request.POST['amount'])
                total=datanum-subamount
                i.balance=total
                i.save()
    return redirect('/')
