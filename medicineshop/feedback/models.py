from django.db import models

# Create your models here.

class feed(models.Model):
    c_id = models.CharField(max_length=30)
    feedbacks=models.CharField(max_length=200)

    def __str__(self):
        return self.c_id
