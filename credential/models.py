from django.db import models

# Create your models here.
class Cad(models.Model):
    name=models.CharField(max_length=250)
    email=models.CharField(max_length=250)
    phone=models.IntegerField(blank=True,null=True)
    message=models.TextField(max_length=500,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.name

class Lux(models.Model):
    luximg=models.ImageField(upload_to='gallery')
    luximgs=models.ImageField(upload_to='gallery')
    luximgss= models.ImageField(upload_to='gallery')
    created_at = models.DateTimeField(auto_now_add=True)

class Luxmodel(models.Model):
    photo=models.ImageField(upload_to='gallery',blank=True, null=True)
    photo1 = models.ImageField(upload_to='gallery',blank=True, null=True)
    photo2 = models.ImageField(upload_to='gallery',blank=True, null=True)
    photooptional = models.ImageField(upload_to='gallery', blank=True, null=True)
    photooptional1 = models.ImageField(upload_to='gallery', blank=True, null=True)
    photooptional2 = models.ImageField(upload_to='gallery', blank=True, null=True)
    luxtitle = models.CharField(max_length=700)
    luxdesc = models.CharField(max_length=500)
    luxloc = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)


class Interior(models.Model):
    interior=models.ImageField(upload_to='gallery')
    created_at = models.DateTimeField(auto_now_add=True)


