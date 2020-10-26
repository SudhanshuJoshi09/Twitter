from django.db import models
from django.conf import settings
import random

User = settings.AUTH_USER_MODEL

# Create your models here.
class Tweet(models.Model):
    """ This defines the content of the tweet. """

     # This is a hidden field.
     # id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE) # Many users have many tweets.
    content = models.TextField()
    image = models.FileField(upload_to='images/', blank=True, null=True)

    class Meta:
        ordering = ['-id']

    """ For getting serialized json format of the model. """
    def serialize(self):
        return {
            "id": self.id,
            "content": self.content,
            "likes": random.randint(0, 1000),
            "image": "/path/to/image"
        }