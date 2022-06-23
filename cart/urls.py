from django.urls import path
from . import views
urlpatterns=[
    path('CartList',views.CartDetails,name='CartList'),
    path('add/<int:product_id>/',views.add_cart,name='addcart'),
    ]