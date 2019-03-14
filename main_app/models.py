from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Dealbreaker(models.Model):
    content = models.CharField(max_length = 100)

    def __str__(self):
        return self.content
    
    def get_absolute_url(self):
        return reverse('dealbreakers_index')

class Bachelor(models.Model): 
    name = models.CharField(max_length = 100)
    age = models.IntegerField()
    wealth_origin = models.TextField(max_length = 250)
    location = models.CharField(max_length = 100)
    net_worth = models.IntegerField()
    dealbreakers = models.ManyToManyField(Dealbreaker)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'bachelor_id': self.id})

class PriorFlame(models.Model):
    name = models.CharField(max_length = 100)
    age = models.IntegerField()
    relationship_duration = models.IntegerField('Together for (in months)')
    breakup_date = models.DateField('Breakup Date')
    bachelor = models.ForeignKey(Bachelor, on_delete=models.CASCADE)

    def __str__(self):
        return f"Don't sweat it! {self.bachelor.name} dumped {self.name} on {self.breakup_date}"
    
class Photo(models.Model):
    url = models.CharField(max_length=200)
    bachelor = models.ForeignKey(Bachelor, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for bachelor_id: {self.bachelor_id} @{self.url}"