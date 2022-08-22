from django.urls import path
from . import views

urlpatterns = [
    path("blogs/list/", views.get_all_blogs_api_view, ),
    path("blogs/create/", views.create_blog_api_view, ),
]
