from django.db import models

"""
posts = Post.objects.all()
posts = Post.objects.get(id=1) только универсальное значение
posts = Post.objects.filter()
"""

class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.name}"
    
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.name}"

class Post(models.Model):
    image = models.ImageField(null=True, blank=True)
    name = models.CharField(max_length=255)
    content = models.CharField(max_length=1000, null=True, blank=True)
    rate = models.IntegerField(default=0, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    # связи
    tags = models.ManyToManyField(Tag, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.name} - {self.content}"