from django.urls import path
from .import views

urlpatterns = [ 
    path('', views.send_the_homepage),
    # path('sign_up/', views.sign_up),
    # path('sign_in/', views.login),
    path('home/', views.send_the_homepage),
    path("shopping-cart/", views.send_the_homepage),
    path("products/",views.send_the_homepage )
]