from django.urls import path
from . import views

app_name = 'authentication'

urlpatterns = [
    path(
        'login',
        views.LoginView.as_view(),
        name='login'
    ),
    path(
        'cadastrar',
        views.CreateUserView.as_view(),
        name='register'
    ),
    path(
        'logout',
        views.LogoutView.as_view(),
        name='logout'
    )
]
