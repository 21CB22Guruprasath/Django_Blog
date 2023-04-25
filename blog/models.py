from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    authour = models.CharField(max_length=20)
    year = models.IntegerField()
    content = models.TextField(max_length=1000)
    
    
    def __str__(self):
        return f'Blog about "{self.title}" by "{self.authour}"'