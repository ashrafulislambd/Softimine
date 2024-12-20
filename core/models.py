from django.db import models

class Query(models.Model):
    name = models.CharField(max_length=500)
    email = models.EmailField()
    details = models.TextField()

    def __str__(self):
        return f"Query from {self.name}"