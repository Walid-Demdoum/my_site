from django.db import models
from django.contrib.auth.models import User

class Vehicle(models.Model):
    name = models.CharField("Marque",max_length=255)
    model_car = models.CharField("Model",max_length=255)
    phone_number = models.CharField("Téléphone",max_length=255,default='+213779675028',blank=True)
    year = models.IntegerField("Année",default=2000)
    boite = models.CharField("Boite de vitesse",max_length=255,choices=[('au','Automatique'),('ma','Manuel')],default="ma")
    energy = models.CharField("Energie",max_length=255,choices=[('essence','Essence'),('diesel','Diesel'),('gpl','GPL')],default='essence')
    description = models.TextField("Description",max_length=1024,default=None,blank=True)
    color = models.CharField("Coleur",max_length=255,default=None,blank=True)
    horse_power = models.CharField("Puissance",max_length=255,default=None,blank=True)
    image = models.ImageField("Image")
    price = models.DecimalField("Prix",max_digits=16, decimal_places=2,blank=True,default=1.00)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="User")

    def __str__(self):
        return self.name
