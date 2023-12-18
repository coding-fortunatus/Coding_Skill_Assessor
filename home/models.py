import uuid
from django.db import models

# Create your models here.


class Language(models.Model):
    id = models.UUIDField(
        primary_key=True, editable=False, default=uuid.uuid4())
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=255)

    def __str__(self) -> str:
        return self.name
