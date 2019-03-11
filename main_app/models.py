from django.db import models

# Create your models here.
class Bachelor(models.Model): 
    name = models.CharField(max_length = 100)
    age = models.IntegerField()
    wealth_origin = models.TextField(max_length = 250)
    location = models.CharField(max_length = 100)
    net_worth = models.IntegerField()
    dealbreaker = models.TextField(max_length = 250)

    def __str__(self):
        return self.name