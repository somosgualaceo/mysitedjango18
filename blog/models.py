from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from users.models import User
from django.conf import settings

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    imagen = models.ImageField(upload_to = 'Post', blank=True)
    imagen2 = models.ImageField(upload_to= 'Post',null=True,blank=True)
    video = models.CharField(max_length=250, blank=True)
    visitas = models.IntegerField(default=-1) 

    def publish(self):
    	self.published_date = timezone.now()
    	self.save()

    def __unicode__(self):
        return self.title
