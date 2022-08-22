from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()


class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) # one to many
    """
    ONE BLOG WILL HAVE ONE USER ONLY,
    BUT
    ONE USER WILL HAVE MULTIpLE BLOGS.
    """
    content = models.TextField()
    title = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

