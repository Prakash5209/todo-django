from django.db import models
from django.conf import settings

class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        
# class Status(models.TextChoices):
#     NOT_FINISHED = 'incomplete','INCOMPLETED'
#     FINISHED = 'completed','COMPLETED'
    
class Task(TimeStampModel):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,blank=True,null=True)
    title=models.CharField(max_length=100)
    description=models.TextField()
    is_completed=models.BooleanField(default=False)
    # status = models.CharField(max_length = 255,choices = Status.choices,default="Status.NOF_FINISHED")
    
    def __str__(self):
        return self.title
    