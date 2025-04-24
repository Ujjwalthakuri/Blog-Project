from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
# Create your models here.

class CategoryModel(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class postModel(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    category = models.ForeignKey(CategoryModel, on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta: 
        ordering = ('-date',)
    
    def comment_count(self):
        return self.comment_set.all().count()
    
    def comments(self):
        return self.comment_set.all()

    def __str__(self):
        return f"{self.title} by {self.author.username if self.author else 'Unknown Author'}"


class profileModel(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='media/default.jpg', upload_to='profile', validators=[FileExtensionValidator(['png', 'jpg'])])
        
    def __str__(self):
        return f'{self.author.username} profile'
        
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(postModel,  on_delete=models.CASCADE)
    content = models.CharField(max_length=50)
    
    def __str__(self):
        return self.content

    
    

