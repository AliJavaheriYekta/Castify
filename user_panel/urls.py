from django.urls import path, include

from user_panel.apis import router
from user_panel.views import LoginView, UserRegistrationView

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('register/', UserRegistrationView.as_view(), name='user_register'),
    path('login/', LoginView.as_view(), name='login'),
]
