import http

from rest_framework.routers import DefaultRouter

from user_panel.views import ProfileViewSet

router = DefaultRouter()
router.register(r'profile', ProfileViewSet, basename='user-profile')

# , basename='follows'