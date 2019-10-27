from django.db import models

# Create your models here.
class posts(models.Model):
    title = models.CharField(max_length=256)
# the bottom declare funtion is mainly used for showing the content present in the object declare above.
    def __str__(self):
        return self.title