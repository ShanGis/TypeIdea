from django.contrib.auth.models import User
from rest_framework import serializers, viewsets

from .models import Post, Category, Tag


class PostSerializer(serializers.HyperlinkedModelSerializer):
    category = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name',
    )
    tag = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name',
    )
    owner = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta():
        model = Post
        fields = (
        'url', 'title', 'dec',  'category', 'created_time', 'owner', 'pv', 'tag'
        )


class PostViewSet(viewsets.ModelViewSet):
        queryset = Post.objects.all()
        serializer_class = PostSerializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta():
        model = Category
        fields = (
            'id', 'name', 'created_time'
        )
    
class CategoryDetailSerializer(serializers.ModelSerializer):
    post_set = PostSerializer(
        many=True,
        read_only=True,
    )
    class Meta():
        model = Category
        fields = (
            'id', 'name', 'created_time', 'post_set'
        )


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.filter(status=1)
    serializer_class = CategorySerializer

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = CategoryDetailSerializer
        return super().retrieve(request, *args, **kwargs)


class TagSerializer(serializers.ModelSerializer):
    class Meta():
        model = Tag
        fields = (
            'id', 'name', 'created_time',
        )


class TagDetailSerializer(serializers.ModelSerializer):
    posts = PostSerializer(
        many=True,
        read_only=True,
    )
    class Meta():
        model = Tag
        fields = (
            'id', 'name', 'created_time', 'posts'
        )


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    
    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = TagDetailSerializer
        return super().retrieve(request, *args, **kwargs)



class UserSerializer(serializers.ModelSerializer):
    class Meta():
        model = User
        fields = (
            'id', 'username',
        )

class UesrDeatilSerializer(serializers.ModelSerializer):
    post_set = PostSerializer(
        many=True,
        read_only=True
    )
    class Meta():
        model = User
        fields = (
            'id', 'username', 'post_set'
        )

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = UesrDeatilSerializer
        return super().retrieve(request, *args, **kwargs)
