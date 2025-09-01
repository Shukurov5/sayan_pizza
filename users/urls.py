from django.urls import path
from .views import LoginView, RegisterView, LogoutView, ProfileView, FeedbackSendView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    # 🔹 Кастомные представления
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('me/', ProfileView.as_view(), name='profile'),
    path('feedback/', FeedbackSendView.as_view(), name='feedback'),

    # 🔹 JWT SimpleJWT
    path('jwt/create/', TokenObtainPairView.as_view(), name='jwt_create'),   # получить access и refresh токены
    path('jwt/refresh/', TokenRefreshView.as_view(), name='jwt_refresh'),    # обновить access токен
    path('jwt/verify/', TokenVerifyView.as_view(), name='jwt_verify'),       # проверить токен
]
