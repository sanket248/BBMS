from django.db import models

# Create your models here.

class Doner_details(models.Model):
    donor_id = models.IntegerField(primary_key=True)
    donor_name = models.CharField(max_length=20)
    contect_no = models.IntegerField(max_length=10)
    blood_group = models.CharField(max_length=3)
    address = models.CharField(max_length=30)
    city = models.CharField(max_length=10)