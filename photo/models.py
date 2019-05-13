from django.db import models

class Location(models.Model):
    name = models.CharField(max_length = 25)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length = 25)

    def __str__(self):
        return self.name

class Images(models.Model):
    image = models.ImageField()
    image_name = models.CharField(max_length =30)
    image_description = models.CharField(max_length =30)
    image_location = models.ForeignKey(Location)
    image_category = models.ForeignKey(Category)  
   
    def __str__(self):
        return self.image

    
    class Meta:
        ordering = ['image']