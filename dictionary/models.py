from django.db import models


class Word(models.Model):
    word = models.CharField(max_length=30, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
