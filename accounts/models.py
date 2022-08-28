from django.db import models
from django.contrib.auth import get_user_model; User = get_user_model()



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, )
    bio = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to="accounts/images", null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username + " |profile"

    def save(self, *args, **kwargs):

        return super().save(*args, **kwargs)
