# blog_backend/urls.py
from django.contrib import admin
from django.urls import path, include
from blog.views import MyTokenObtainPairView, health_check  # updated import
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', health_check),  # NEW: root endpoint
    path('api/', include('blog.urls')),  # e.g., /api/blogs/
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
