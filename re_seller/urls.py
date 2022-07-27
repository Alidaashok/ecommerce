from django.urls import path
from . import views
urlpatterns=[
    path('addprodct',views.addproduct),
    path('reseller-home',views.resellerhome),
    path('view-order',views.vieworder),
    path('view-payment',views.viewpayment)
]