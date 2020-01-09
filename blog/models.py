from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField


# Post model
class Post(models.Model):
    # id = models.CharField(primary_key=True, max_length=80)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    # tags = ArrayField(models.CharField(max_length=80, blank=True), size=3)

    def __str__(self):
        return self.title
