from django.shortcuts import render

# Create your views here.
def addproduct(request):
    return render(request,'re_seller/addproduct.html')
def resellerhome(request):
    return render(request,'re_seller/resellerhome.html')
def vieworder(request):
    return render(request,'re_seller/vieworder.html')
def viewpayment(request):
    return render(request,'re_seller/viewpayment.html')