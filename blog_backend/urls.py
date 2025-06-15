from django.contrib import admin
from django.urls import path, include
from blog.views import health_check

urlpatterns = [
    path('admin/', admin.site.urls),
    path('health/', health_check),               # ✅ Health check endpoint
    path('api/', include('blog.urls')),          # ✅ API routes
]
