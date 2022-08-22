from ..models import Blog
from django.contrib.auth import get_user_model
from django.http import JsonResponse  # renderer

# imports from rest_framework
from rest_framework.decorators import api_view

User = get_user_model()

# [] --> array
# {} --> object


@api_view(http_method_names=["GET", ])
def get_all_blogs_api_view(request):
    context = []
    blog_qs = Blog.objects.all()
    counter = blog_qs.count()
    for blog in blog_qs:
        obj = {}
        user = blog.user
        obj["user"] = {
            "id": user.id,  # ctrl + D
            "username": user.username,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
        }
        obj["title"] = blog.title
        obj["content"] = blog.content

        context.append(obj)

    response = {
        "count": counter,
        "data": context
    }


    return JsonResponse(response, safe=False)


@api_view(http_method_names=["post", ])
def create_blog_api_view(request):
    data = request.data
    print(data)

    user_id = data.get("user")
    blog_user = User.objects.get(id=user_id)  # getting user by id
    blog_title = data.get("title")
    blog_content = data.get("content")

    blog_obj = Blog.objects.create(user=blog_user, title=blog_title, content=blog_content)
    print(blog_obj)

    obj = {}
    user = blog_obj.user
    obj["user"] = {
        "id": user.id,  # ctrl + D
        "username": user.username,
        "email": user.email,
        "first_name": user.first_name,
        "last_name": user.last_name,
    }
    obj["title"] = blog_obj.title
    obj["content"] = blog_obj.content
    
    response = {
        "status": "created",
        "data": obj
    }

    return JsonResponse(response, safe=True)