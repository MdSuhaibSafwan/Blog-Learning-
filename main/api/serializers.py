from rest_framework import serializers
from ..models import Blog


class BlogSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Blog
        fields = "__all__"
        # exclude = ["user", ]
