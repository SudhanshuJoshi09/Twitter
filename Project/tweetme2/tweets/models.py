from django.db import models
import random

# Create your models here.
class Tweet(models.Model):
    """ This defines the content of the tweet. """

     # This is a hidden field.
     # id = models.AutoField(primary_key=True)
    content = models.TextField()
    image = models.FileField(upload_to='images/', blank=True, null=True)

    """ For getting serialized json format of the model. """
    def serialize(self):
        return {
            "id": self.id,
            "content": self.content,
            "likes": random.randint(0, 1000),
            "image": "/path/to/image"
        }