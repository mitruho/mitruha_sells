from django.db import models
from ckeditor.fields import RichTextField

class Item(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='Items/', default='Items/default.png')
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    price = models.IntegerField()

    def __str__(self):
        return self.title
    
class AboutPage(models.Model):
    content = RichTextField()

    def __str__(self):
        return "about_page"