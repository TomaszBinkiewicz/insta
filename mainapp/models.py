from django.db import models


class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField(max_length=20)
    password = models.TextField(max_length=20)


class Image(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.TextField(max_length=64)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    path = models.TextField(max_length=64)


class Comment(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    content = models.TextField(max_length=255)
