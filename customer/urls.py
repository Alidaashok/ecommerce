from django.urls import path
from . import views
urlpatterns=[
    path('cartpage',views.cart),
    path('custhom',views.custhome),
    path('ORDER',views.ORDER),
    path('productdetails',views.productdetails),
    path('viewproduct',views.viewproduct),
    path('shhome',views.showhome)
]