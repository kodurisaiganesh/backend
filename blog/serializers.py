from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import Blog

# ✅ Include full author info
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class BlogSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    is_owner = serializers.SerializerMethodField()  # ✅ Add this field

    class Meta:
        model = Blog
        fields = [
            'id', 'title', 'slug', 'content', 'created_at', 'updated_at',
            'is_published', 'author', 'is_owner'  # ✅ include is_owner
        ]
        read_only_fields = ['author', 'slug', 'created_at', 'updated_at']

    def get_is_owner(self, obj):
        request = self.context.get('request', None)
        if request and request.user and not request.user.is_anonymous:
            return obj.author == request.user  # ✅ Check ownership
        return False

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        return User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        token['email'] = user.email
        token['user_id'] = user.id  # ✅ Add user ID for easier use in frontend
        return token
