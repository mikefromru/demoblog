from django.db import models

class Article(models.Model):
    
    title = models.CharField(max_length=255)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        
        ordering = ['-created']

    def __str__(self):
        return self.title