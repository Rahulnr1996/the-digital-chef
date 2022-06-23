from django.urls import path
from . import views
urlpatterns=[
    path('reg',views.register,name='reg'),
    path('log',views.login,name='log'),

    ]