from django.db import models

class Location(models.Model):
    name = models.CharField(max_length = 25)

    

    def save_location(self):
        self.save()
        
class Category(models.Model):
    name = models.CharField(max_length = 25)

   

class Images(models.Model):
    image = models.ImageField(upload_to="images/")
    image_name = models.CharField(max_length =30)
    image_description = models.CharField(max_length =30)
    image_location = models.ForeignKey(Location)
    image_category = models.ForeignKey(Category)  
   
   

    def save_editor(self):
        self.save()
    
    class Meta:
        ordering = ['image']