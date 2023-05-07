from django.db import models
from django.conf import settings

class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-modified_at' ,'-created_at']
    
class Task(TimeStampModel):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,blank=True,null=True)
    title=models.CharField(max_length=100)
    description=models.TextField()
    
    def __str__(self):
        return self.title
    