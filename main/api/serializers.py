from rest_framework import serializers
from ..models import Blog
from accounts.api.serializers import UserSerializer


class BlogSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    is_blog_user = serializers.SerializerMethodField()  # function
    
    class Meta:
        model = Blog
        fields = "__all__"
        # exclude = ["user", ]

    def get_is_blog_user(self, obj):
        h = self.context.get("hello")
        print("Blog", obj, h)
        return None
