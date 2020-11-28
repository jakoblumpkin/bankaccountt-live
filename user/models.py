from django.db import models

# Create your models here.

class account(models.Model):
    username=models.CharField(max_length=200, null=True)
    balance=models.DecimalField(max_digits=19, decimal_places=2)

    def __str__(self):
        return self.username

class usernames(models.Model):
    names=models.CharField(max_length=200, null=True)