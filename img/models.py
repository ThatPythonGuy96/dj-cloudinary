from django.db import models
from cloudinary.models import CloudinaryField

class Image(models.Model):
    img = CloudinaryField('image', folder='images/')

