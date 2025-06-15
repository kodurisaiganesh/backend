# blog/views.py

from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse

from .models import Blog
from .serializers import BlogSerializer, RegisterSerializer, MyTokenObtainPairSerializer
from .permissions import IsAuthorOrReadOnly  # ✅ import custom permission

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthorOrReadOnly]  # ✅ use custom permission

    def perform_create(self, serializer):
        # ✅ Automatically assign the logged-in user as author
        serializer.save(author=self.request.user)

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.create(
                username=serializer.validated_data['username'],
                email=serializer.validated_data['email'],
                password=make_password(serializer.validated_data['password'])
            )
            return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

def health_check(request):
    return JsonResponse({"status": "ok"})
