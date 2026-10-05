from django.db import models
from django.contrib.auth.models import AbstractUser
#from blogs.views import *

# Create your models here.
class UserModel(AbstractUser):
    full_name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return f'{self.username}'
    

class BlogModel(models.Model):

    CATAGORY = [
        ('Education','Education'),
        ('Techlonogy','Technology'),
        ('Sports','Sports'),
    ]

    title = models.TextField(null=True)
    author_name = models.CharField(max_length=200, null=True)
    content = models.TextField(null=True)
    catagory = models.CharField(choices=CATAGORY, max_length=20, null=True)
    blog_image = models.ImageField(upload_to='media/blog_img', null=True)
    publish_date = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
            return f'{self.title}'
        
