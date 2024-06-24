from django.urls import path
from .views import RegisterUser, UserLogin, UserLogout

urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', UserLogout.as_view(), name='logout')
    ]
