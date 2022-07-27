from django.shortcuts import render

# Create your views here.
def adminhome(request):
    return render(request,'e_comadmin/adminhome.html')
def approve(request):
    return render(request,'e_comadmin/approve.html')
def view_customer(request):
    return render(request,'e_comadmin/view_customer.html')
def viewseller(request):
    return render(request,'e_comadmin/viewseller.html')

