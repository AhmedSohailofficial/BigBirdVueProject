from django.db import models

# Create your models here.
class SecondProducts(models.Model):
    image=models.ImageField(upload_to="Secondproducts/", blank=True)
    MainText=models.CharField(max_length=200)
    SubText=models.CharField(max_length=200)
    
    def __str__(self):
        return self.MainText