from django.db import models

class Images(models.Model):
    image = models.ImageField()
    image_name = models.CharField(max_length =30)
    image_description = models.CharField(max_length =30)
    image_location = models.ImageField()
    image_category = models.ImageField()  
   
   def __str__(self):
        return self.image

    
    class Meta:
        ordering = ['image']
    

   try:
        images = Image.objects.get(image)
        print('Images found')
      except DoesNotExist:
          print('Images was not found')