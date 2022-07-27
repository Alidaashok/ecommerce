from django.urls import path
from . import views
urlpatterns=[
    path('adminhome',views.adminhome),
    path('approve',views.approve),
    path('view_customer',views.view_customer),
    path('viewseller',views.viewseller)
]