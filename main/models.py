from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.utils import timezone

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
    
    def how_old_blog_is(self):
        t1 = self.date_created
        t2 = timezone.now()

        elapsed = t2 - t1

        return elapsed


class BlogImages(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="blog")
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.blog)

    class Meta:
        verbose_name_plural = "Blog Images"
