from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class career(models.Model):
      firstname = models.CharField(max_length= 20)
      lastname = models.CharField(max_length= 20)
      email = models.EmailField()
      phone = PhoneNumberField(max_length=13)
      position = models.CharField(max_length=50, choices=(
            ("Network Engineer","Network Engineer"),
            ("Sale Excutive","Sale Excutive"),
            
      ))
      experience = models.CharField(max_length=50, choices=(
            ("Fresher","Fresher"),
            ("1 Year","1 Year"),
            ("2 Year","2 Year"),
            ("3+ Year","3+ Year"),
      ))
      join = models.CharField(max_length=50, choices=(
            ("Right now","Right now"),
            ("In a few week","In a few week"),
            ("In a few month","In a few month"),
            ("No Sure","No Sure"),
      ))
      description = models.TextField(max_length=10000)
      document = models.FileField(upload_to="img/career/")


      def __str__(self):
            return self.firstname + ' ' + self.lastname