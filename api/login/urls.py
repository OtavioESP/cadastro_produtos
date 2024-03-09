from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenObtainSlidingView,
)

urlpatterns = [
    path('login', TokenObtainPairView.as_view(), name='obtem_token'),
    path('login/atualizar', TokenRefreshView.as_view(), name='atualiza_token')
]
