from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager


# Create your models here.
class Category (models.Model):
    name = models.CharField(max_length= 200)
    def __str__(self):
        return self.name
    

class Post (models.Model):
    author= models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    image = models.ImageField(upload_to='blog/', default='blog\defult.jpg')
    title = models.CharField(max_length= 255)
    content = models.TextField()
    category = models.ManyToManyField(Category)
    tag = TaggableManager()
    counted_view = models.IntegerField(default=0)
    published_status = models.BooleanField(default=False)
    login_require = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(null=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_date']

    def get_absolute_url(self):
        return reverse ('blog:single', kwargs={'pid':self.id})
    

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    approve = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-created_date']