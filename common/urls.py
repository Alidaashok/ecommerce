from django.urls import path
from . import views
app_name='common'
urlpatterns=[
    path('Admin-login', views.Admin_login,name='admin_login'),
    path('customer-login', views.cust_login,name='customer_login'),
    path('cust_sign_up',views.cust_sign_up,name='customer_sign_up'),
    path('projecthome',views.projecthome),
    path('Reseller_login',views.Reseller_login),
    path('reseller_sign_up',views.reseller_sign_up)

]