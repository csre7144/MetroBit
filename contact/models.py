from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class ContactList(models.Model):
      name = models.CharField(max_length=50)
      email = models.EmailField()
      phone = PhoneNumberField(blank=True)
      message = models.TextField(max_length=1000)

      def __str__(self):
            return self.name