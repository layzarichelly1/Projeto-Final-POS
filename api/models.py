from django.db import models

class User(models.Model):
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    addres = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Todo(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    completed = models.BooleanField(False)

class Comment(models.Model):
    postId = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    body = models.CharField(max_length=200)

    def __str__(self):
        return self.nome
    
class Post(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
