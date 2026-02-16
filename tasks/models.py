from django.db import models

class Task(models.Model):   # Capitalized, singular
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
