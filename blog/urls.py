from django.urls import path
from .views import (
    BlogListCreateAPIView,
    BlogRetrieveUpdateDestroyAPIView,
    RegisterView,
    MyTokenObtainPairView,
    health_check
)
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('blogs/', BlogListCreateAPIView.as_view(), name='blog-list-create'),               # /api/blogs/
    path('blogs/<int:pk>/', BlogRetrieveUpdateDestroyAPIView.as_view(), name='blog-detail'),# /api/blogs/1/
    path('register/', RegisterView.as_view(), name='register'),                             # /api/register/
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),              # /api/token/
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),               # /api/token/refresh/
    path('health/', health_check),                                                          # /api/health/
]
