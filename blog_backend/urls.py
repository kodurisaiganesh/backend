# blog_backend/urls.py

from django.contrib import admin
from django.urls import path, include
from blog.views import health_check

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', health_check),  # Optional: Health check at root
    path('api/', include('blog.urls')),  # Route all /api/ endpoints to blog app
]
