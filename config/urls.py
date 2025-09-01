"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# config/urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView



urlpatterns = [
    path('admin/', admin.site.urls),

    # 🔹 API приложений с отдельными префиксами
    path('api/menu/', include('menu.urls')),         # блюда и отзывы
    path('api/bookings/', include('booking.urls')),  # бронирования столиков
    path('api/auth/', include('users.urls')),       # регистрация, логин, пользователи
    path('api/cart/', include('cart.urls')),        # корзина
]

# 🔹 Swagger / ReDoc
urlpatterns += [
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),                   # JSON OpenAPI
    path('api/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),  # Swagger UI
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),           # ReDoc
]

# 🔹 Статика и медиа файлы в режиме DEBUG
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
