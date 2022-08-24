from django.core.exceptions import MultipleObjectsReturned
from rest_framework.exceptions import NotFound, ValidationError
from .models import Blog

# Not Found --> 404
# Validation Error --> 400


def get_object_or_rest_404(klass, **kwargs):
    qs = klass.objects.filter(**kwargs)
    if not qs.exists():
        raise NotFound(f"{klass} with this info is not found")
    try:
        return qs.get()
    except MultipleObjectsReturned:
        return qs
