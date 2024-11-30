from django.db import models

class Post(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField(max_length=20)
    slug = models.SlugField(max_length=255, null=True, blank=True)


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    body = models.TextField()


class Item(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField(max_length=20)
