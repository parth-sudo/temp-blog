from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextField(blank=True, null=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author")
    likes = models.ManyToManyField(User, related_name="likes")

    def __str__(self):
        return self.title
    
    def total_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk}) #to form a post and redirect to post-detail.
    

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    body = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    writer = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name="writer")

    def __str__(self):
        return '%s - %s' %(self.post.title, self.name)