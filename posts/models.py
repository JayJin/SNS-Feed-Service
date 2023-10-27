from django.db import models
from users.models import UserModel

# Create your models here.
class PostModel(models.Model):
    content_id = models.CharField(max_length=32, unique=True, null=False)
    type = models.CharField(max_length=128, null=False)
    title = models.CharField(max_length=256, null=False)
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    content = models.CharField(max_length=256)
    # hashtags = 
    # view_count = 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # is_deleted = 
    
    def __str__(self):
        return str(self.title)
    
    class Meta:
        db_table = 'post'
        ordering = ['-created_at']    