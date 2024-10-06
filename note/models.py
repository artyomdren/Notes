from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class NoteModel(models.Model):

    head = models.TextField(max_length=50, db_index=True, null=False)
    memo = models.TextField(max_length=100, db_index=True)
    published_at = models.DateTimeField(auto_now_add=True)

