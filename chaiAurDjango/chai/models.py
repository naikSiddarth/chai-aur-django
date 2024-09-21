from django.db import models
from django.utils import timezone

class ChaiType(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='chais/')
    time = models.DateTimeField(default=timezone.now)
    
    def __str__(self) -> str:
        return self.name