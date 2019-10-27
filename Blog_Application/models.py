from django.db import models

# Create your models here.
class posts(models.Model):
    title = models.CharField(max_length=256)
# the bottom declared funtion is mainly used for showing the content present in the object declared above.
    def __str__(self):
        return self.title