from django.db import models
import datetime as dt


class Location(models.Model):
    name = models.CharField(max_length = 25)

    

    def save_location(self):
        self.save()
        
class Category(models.Model):
    name = models.CharField(max_length = 25)

   

class Image(models.Model):
    image = models.ImageField(upload_to="images/")
    image_name = models.CharField(max_length =30)
    image_description = models.CharField(max_length =30)
    image_location = models.ForeignKey(Location)
    image_category = models.ForeignKey(Category)  
   
    def __str__(self):
        return self.image_name
    class Meta:
        ordering = ['image']

    def save_image(self):
        self.save()

    @classmethod
    def get_image_by_id(cls):
        images = cls.objects.get(pk=id)
        return images

    @classmethod
    def search_by_image_category(cls,search_term):
        images = cls.objects.filter(image_icontains=search_terms)
        return images 