from django.db import models

# Create your models here.
class Todo(models.Model):
    quest = models.CharField(max_length=40)
    isComplete = models.BooleanField(default=False)

    def __str__(self):
        return self.quest