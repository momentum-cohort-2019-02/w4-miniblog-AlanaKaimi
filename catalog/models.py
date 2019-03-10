from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.urls import reverse

# Create your models here.


class Blogger(models.Model):
    """Model representing a blogger"""
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50)
    user_bio = models.CharField(max_length=200)


    class Meta:
        ordering = ['user_name']

    def get_absolute_url(self):
        """Returns the url to access a particluar author instance"""
        return reverse('blogger-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object"""
        return f'{self.last_name}, {self.first_name}'


class BlogPost(models.Model):
    """Model representing a blogpost"""
    title = models.CharField(max_length=100)
    
    # Foreign Key used because blog posts can only have one blogger, but bloggers can have multiple blog posts
    # Blogger as a string rather than object because it hasn't been declared yet in the file
    blogger = models.ForeignKey('Blogger', on_delete=models.SET_NULL, null=True)
    
    # auto_now=True Sets the field to the current date every time the model is saved
    post_date = models.DateTimeField(auto_now=True)

    content = models.TextField(max_length=1000, help_text='Share your thoughts here')

    class Meta:
        ordering = ['title', 'post_date', 'blogger']

    def get_absolute_url(self):
        """Returns the url to access a detailed record of post"""
        return reverse('blogpost-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object"""
        return self.title


# class Comments(models.Model):