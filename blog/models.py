from unittest.util import _MAX_LENGTH
from django.db import models

# Post model
class Post(models.Model):
        title = models.CharField(max_length=30)
        content = models.TextField()

        created_at = models.DateTimeField()

        def __Str__(self):
            return self.title