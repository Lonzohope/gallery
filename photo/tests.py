from django.test import TestCase
from .models import Images

class ImagesTestClass(TestCase):

    # Set up method
       def setUp(self):
        self.image= Images()

        #Testing instance
        def test_instance(self):
         self.assertTrue(isinstance(self.image,Editor))  
         

        # Testing Save Method
        def test_save_method(self):
            self.image.save_images()
            images = Images.objects.all()
            self.assertTrue(len(images) > 0)
