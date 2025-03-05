# analytics/models.py
from django.db import models
from django.contrib.auth.models import User
from blog_app.models import BlogPost

class PageView(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='views')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"View of {self.post.title} by {self.user or 'Anonymous'}"