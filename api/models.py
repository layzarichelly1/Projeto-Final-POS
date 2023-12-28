from django.db import models

class User(models.Model):
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    addres = models.CharField(max_length=250)
    phone = models.CharField(max_length=11)
    website = models.CharField(max_length=200)
    company = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Todos(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    completed = models.BooleanField(False)

    
class Post(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=200)

class Comment(models.Model):
    postId = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    body = models.CharField(max_length=200)