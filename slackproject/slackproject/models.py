from django.db import models

class slackdetaisl(models.Model):
    slackUsername = models.CharField(max_length=200)
    backend = models.BooleanField(default=True)
    age = models.IntegerField()
    bio = models.CharField(max_length=1000)

    def __str__(self):
        return  self.slackUsername