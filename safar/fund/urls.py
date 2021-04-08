from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
	path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('causes', views.causes, name="causes"),
    path('causes-details', views.causes_details, name="causes-details"),
    path('sign-in', views.sign_in, name="Signin"),
    path('sign-up', views.sign_up, name="SignUp"),
    path('adminSignin', views.admin_sign_in, name="AdminSignin")
]

