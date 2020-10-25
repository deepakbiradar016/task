from django.db import models


class JsonData(models.Model):

    userId = models.IntegerField()
    id = models.IntegerField(unique=True, primary_key=True)
    title = models.CharField(max_length=150)
    body = models.TextField()

    def __str__(self):
        return str(self.title)

