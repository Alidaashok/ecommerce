from django.shortcuts import render

# Create your views here.

def Admin_login(request):
    return render(request,'common/Admin_login.html')
def cust_login(request):
     return render(request,'common/cust_login.html')
def cust_sign_up(request):
     return render(request,'common/cust_sign_up.html')
def projecthome(request):
     return render(request,'common/projecthome.html')
def Reseller_login(request):
     return render(request,'common/Reseller_login.html')
def reseller_sign_up(request):
     return render(request,'common/reseller_sign_up.html')
