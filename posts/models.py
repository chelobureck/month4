from django.db import models

"""
posts = Post.objects.all()
posts = Post.objects.get(id=1) только универсальное значение
posts = Post.objects.filter()
"""

class Post(models.Model):
    name = models.CharField(max_length=255)
    contet = models.CharField(max_length=1000, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self) -> str:
        return f"{self.name} - {self.contet}"