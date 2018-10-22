from django.db import models
from django.contrib import admin


class BlogPost(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=75)
    date = models.DateTimeField(auto_now=True)
    post = models.CharField(max_length=2500)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    pass