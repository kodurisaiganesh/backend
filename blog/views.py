from rest_framework import generics, permissions, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from django.http import JsonResponse
from .models import Blog
from .serializers import BlogSerializer


# ✅ Health Check View
def health_check(request):
    return JsonResponse({"status": "ok"})


# ✅ List and Create View
class BlogListCreateAPIView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_context(self):
        return {'request': self.request}

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


# ✅ Retrieve, Update, and Destroy View with Author Permissions
class BlogRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_context(self):
        return {'request': self.request}

    def perform_update(self, serializer):
        blog = self.get_object()
        if blog.author != self.request.user:
            raise PermissionDenied("You are not the author of this blog.")
        serializer.save()

    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise PermissionDenied("You are not the author of this blog.")
        instance.delete()
