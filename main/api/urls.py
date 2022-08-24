from django.urls import path
from . import views

urlpatterns = [
    path("blogs/list-create/", views.BlogListCreateAPIView.as_view(), ),
    # path("blogs/create/", views.create_blog_api_view, ),
    path("blogs/update/<int:blog_id>/", views.BlogRetrieveUpdateDestroyAPIView.as_view(), )
]
