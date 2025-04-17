from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
# Create your models here.

class postModel(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta: 
        ordering = ('-date',)

    def __str__(self):
        return f"{self.title} by {self.author.username if self.author else 'Unknown Author'}"


class profileModel(models.Model):
        author = models.OneToOneField(User, on_delete=models.CASCADE)
        image = models.ImageField(default='media/default.jpg', upload_to='profile', validators=[FileExtensionValidator(['png', 'jpg'])])
        
        def __str__(self):
            return f'{self.author.username} profile'

    
    

