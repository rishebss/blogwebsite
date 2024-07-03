from django.db import models
# Create your models here.
class  Complete(models.Model):
    photo = models.ImageField(upload_to='gallery', blank=True, null=True)
    photo1 = models.ImageField(upload_to='gallery', blank=True, null=True)
    photo2 = models.ImageField(upload_to='gallery', blank=True, null=True)
    photooptional = models.ImageField(upload_to='gallery', blank=True, null=True)
    photooptional1 = models.ImageField(upload_to='gallery', blank=True, null=True)
    photooptional2 = models.ImageField(upload_to='gallery', blank=True, null=True)
    pic=models.ImageField(upload_to='gallery')
    title=models.CharField(max_length=700)
    location=models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



class  Incomplete(models.Model):
    photo = models.ImageField(upload_to='gallery', blank=True, null=True)
    photo1 = models.ImageField(upload_to='gallery', blank=True, null=True)
    photo2 = models.ImageField(upload_to='gallery', blank=True, null=True)
    photooptional = models.ImageField(upload_to='gallery', blank=True, null=True)
    photooptional1 = models.ImageField(upload_to='gallery', blank=True, null=True)
    photooptional2 = models.ImageField(upload_to='gallery', blank=True, null=True)
    picture=models.ImageField(upload_to='gallery')
    heading=models.CharField(max_length=700)
    place=models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.heading