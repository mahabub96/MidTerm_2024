from django.db import models

# Create your models here.


class Subscription(models.Model):
    user = models.CharField(max_length=100)  # Just a string for simplicity
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.user}'s subscription"
