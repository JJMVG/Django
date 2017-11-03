from django.db import models
from django.core.urlresolvers import reverse

class Person(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=254,blank=True)
    drink_choices = (('C','Coffee'),('T','Tea'),)
    drink = models.CharField(max_length=1,choices=drink_choices,default='Tea')
    milk = models.BooleanField(default=True)
    sugar = models.BooleanField(default=True)
    profile_picture = models.FileField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('teasite:detail',kwargs={'pk': self.pk})

