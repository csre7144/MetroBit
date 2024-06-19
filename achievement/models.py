from django.db import models

# Create your models here.
class achievement(models.Model):
      img = models.ImageField()
      description = models.TextField(max_length=50000)

      def __str__(self):
            return self.description