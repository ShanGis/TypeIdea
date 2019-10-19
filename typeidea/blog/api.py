import logging

from django.contrib.auth.models import User
from rest_framework import serializers, viewsets, pagination

from .models import Post, Category, Tag

logger = logging.getLogger(__name__)


class PostSerializer(serializers.HyperlinkedModelSerializer):
    category = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name',
    )
    created_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    class Meta():
        model = Post
        fields = (
        'url', 'title', 'dec', 'category', 'created_time', 'pv', 
        )


class PostViewSet(viewsets.ModelViewSet):
        queryset = Post.objects.all()
        serializer_class = PostSerializer

        def get_queryset(self):
            qs = super().get_queryset()
            category_id = self.request.GET.get('category')
            logger.info(category_id)
            if category_id:
                qs = qs.filter(category_id=category_id)
            logger.info(qs)
            return qs

        def retrieve(self, request, *args, **kwargs):
            self.serializer_class = PostDetailSerializer
            return super().retrieve(request, *args, **kwargs)


class CategorySerializer(serializers.ModelSerializer):
    created_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')

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
    created_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')

    class Meta():
        model = Tag
        fields = (
            'id', 'name', 'created_time',
        )


class TagDetailSerializer(serializers.ModelSerializer):
    posts = serializers.SerializerMethodField('paginated_posts')

    def paginated_posts(self, obj):
        posts = obj.posts.all()
        paginator = pagination.PageNumberPagination()
        pag = paginator.paginate_queryset(posts, self.context['request'])
        serializer = PostSerializer(pag, many=True, context={'request': self.context['request']})
        return {
            'count': posts.count(),
            'result': serializer.data,
            'previous': paginator.get_previous_link(),
            'next': paginator.get_next_link(),
        }


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


class PostDetailSerializer(serializers.HyperlinkedModelSerializer):
    tag = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name',
    )
    owner = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )
    
    tag = TagSerializer(
        many=True,
        read_only=True,
    )

    class Meta():
        model = Post
        fields = (
        'url', 'owner', 'title', 'dec', 'category', 'tag', 'created_time', 'pv', 
        )