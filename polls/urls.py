from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("<int:vehicle_id>",views.detail,name="detail"),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name= "logout"),
    path("vehicleForm", views.vehicleForm, name= "vehicleForm"),
    #google
    path('accounts/', include('allauth.urls')),
    path('auth/', include('allauth.socialaccount.urls')),
]