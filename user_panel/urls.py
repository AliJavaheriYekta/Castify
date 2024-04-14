from django.urls import path

from user_panel.views import LoginView, UserRegistrationView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user_register'),
    path('login/', LoginView.as_view(), name='login'),
]
