from django.db import models
from django.contrib.auth.models import User

class JsonData(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    userId = models.IntegerField()
    id = models.IntegerField(unique=True,primary_key=True)
    title = models.CharField(max_length=150)
    body = models.TextField()

    def __str__(self):
        return str(self.title)

