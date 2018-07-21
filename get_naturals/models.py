from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class Channels(models.Model):
	
	channel = models.CharField(max_length=200)
	distr = models.CharField(max_length=50, default = "National")
	tvr = models.FloatField()
	affinity = models.FloatField()
	tcpp = models.FloatField()
	mandatory_placement = models.CharField(max_length = 10)
	prime_time = models.FloatField()
