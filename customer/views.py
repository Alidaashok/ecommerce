from django.shortcuts import render

# Create your views here.
def cart(request):
    return render(request,'customer/cart.html')
def custhome(request):
    return render(request,'customer/custhome.html')
def ORDER(request):
    return render(request,'customer/ORDER.html')
def productdetails(request):
    return render(request,'customer/productdetails.html')
def viewproduct(request):
    return render(request,'customer/viewproduct.html')
def showhome(request):
    return render(request,'customer/showhome.html')    


