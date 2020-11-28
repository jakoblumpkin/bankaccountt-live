from .models import *

# function that adds commas to number for display
def addcommas(number):
    number="{:.2f}".format(number)
    afterdigits=str(number)[::-1][:3][::-1]
    string=''
    num=0
    thelist=[]
    result=list(str(number)[::-1][3:])
    position=[i for i in range(1,len(str(number)),3)]
    for i in result:
        num=num+1
        if num in position:
            thelist.append(',')
            thelist.append(i)
        else:
            thelist.append(i)
    for i in thelist[1:][::-1]:
        string=string+i
    print(result)
    return string+afterdigits
    # return afterdigits

def finduser(username):
    accounts=account.objects.all()
    for i in accounts:
        if str(i.username)==str(username):
            return i.balance
    account.objects.create(username=username, balance=0.0)
    return 'Created'

def addtodata(number, user):
    accounts = account.objects.all()
    for i in accounts:
        if str(i.username)==str(user):
            amount=i.balance
            totnumber=float(number)+float(amount)
            i.balance=totnumber
            i.save()
            return 'added'