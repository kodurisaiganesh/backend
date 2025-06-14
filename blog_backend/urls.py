from django.contrib import admin
from django.urls import path, include
from blog.views import MyTokenObtainPairView, RegisterView, health_check
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', health_check),  # ✅ Root check
    path('api/', include('blog.urls')),  # ✅ Blog + register APIs under /api/
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register/', RegisterView.as_view(), name='register'),  # ✅ Add register
]
