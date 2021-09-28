from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(default=datetime.now)



    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural ='Categories'    

class Post(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    thumbnail = models.ImageField(upload_to='post/thumbnail')
    description = RichTextField(null=True,blank=True)
    tags = models.TextField()
    posted = models.DateField(default=datetime.now)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE ,related_name="comments")
    name = models.CharField(max_length=100)
    comments = models.TextField(max_length=100,default='')
    email = models.EmailField(max_length=100,null=True,blank=True)
    created = models.DateTimeField(default=datetime.now)
    weburl = models.CharField(max_length=100,null=True,blank=True)
    is_resolved = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"