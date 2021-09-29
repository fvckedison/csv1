from django.db import models
# Create your models here.


class Profile(models.Model):
    number = models.CharField(max_length=100,default='')
    photoName = models.CharField(max_length=10,default='')
    filter = models.CharField(max_length=4,default='')
    shootingDate = models.CharField(max_length=10,default='')
    shootinLocation = models.CharField(max_length=4,default='')
    width = models.CharField(max_length=10,default='')
    strain = models.CharField(max_length=4,default='')
    height = models.CharField(max_length=10,default='')
    camera = models.CharField(max_length=20,default='')
    shootingTime = models.CharField(max_length=20,default='')
    exposureTime = models.CharField(max_length=5,default='')
    aperture = models.CharField(max_length=2,default='')
    exposure = models.CharField(max_length=20,default='')
    ISO = models.CharField(max_length=5,default='')
    focalLength = models.CharField(max_length=5,default='')
    shootingArea = models.CharField(max_length=10,default='')
    disease = models.CharField(max_length=10,default='')
    plantsNumber = models.CharField(max_length=10,default='')
    shootingFunction = models.CharField(max_length=10,default='')
    filename = models.CharField(max_length=15,default='')
    def __str__(self):
        return self.filename+'_'+self.number

