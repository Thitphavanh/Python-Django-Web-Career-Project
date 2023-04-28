from django.db import models
from email.policy import default
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=160)
    email = models.EmailField()
    sender = models.CharField(max_length=80)
    detail = models.TextField()
    date_sent = models.DateTimeField(auto_now_add=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    


    def __str__(self):
        return self.title
    

class Portal(models.Model):
    title = models.CharField(max_length=100)
    detail = models.TextField()
    file = models.FileField(upload_to='files/')
    tag = models.TextField(blank=True, null=True)
    email = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.title
    
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="photoprofile", null=True, blank=True, default='default.png')
    usertype = models.CharField(max_length=100, default='member')
    cartquan = models.IntegerField(default=0)