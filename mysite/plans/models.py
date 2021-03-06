from django.conf import settings
from django.contrib import auth
from django.db import models
from django.http import request
from stores.models import Store

category = [('Regular', 'Regular'), ('Exclusive', 'Exclusive'), ('Premium', 'Premium'), ]



# Create your models here.
class Plan(models.Model):
    name = models.CharField(max_length=200, default="Plan Name")
    category = models.CharField(max_length=200, choices=category, default='Regular')
    mealDescription = models.TextField(max_length=2000, default=
                                    "Saturday : Rice + Egg + Veg "+"\n"+
                                    "Sunday :  Rice + Fish + Veg \n"+"\n"+
                                   "Monday :  Rice + Chicken + Veg \n"+"\n"+
                                   "Tuesday : Rice + Mutton + Veg \n"+"\n"+
                                   "Wednesday :  Rice + Fish + Veg \n"+"\n"+
                                   "Thursday : Rice + Chicken + Veg \n"+"\n"+
                                   "Friday :  Biriyani\n"+"\n"
                                  )
    foodphoto=models.ImageField(default='default.gif', upload_to='plans', blank=True)
    price = models.FloatField(max_length=200, default=39.99)
    store = models.ForeignKey(Store, default=None, on_delete=models.CASCADE)
