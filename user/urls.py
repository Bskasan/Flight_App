
from django.urls import path, re_path, include

urlpatterns = [
    path('auth/', include('dj_rest_auth.urls'))
]

# ----------------------------- ROUTER ---------------------------- #
from rest_framework.routers import DefaultRouter
from .views import (
    UserView,
    UserCreateView,
)

router = DefaultRouter()
router.register('create', UserCreateView) # permissions.AllowAny
router.register('', UserView) # permissions.IsAdminUser
urlpatterns += router.urls
