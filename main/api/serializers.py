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
        # h = self.context.get("hello")  # key
        # print("Blog", obj, h)
        print("Blog --> ", obj)
        request = self.context.get("request", None) ## either get the request or set it to None
        if not request:
            return None  #JSON None --> null, True --> true, False --> false
        
        # current auth user from the views
        return obj.user == request.user  # either true or false
