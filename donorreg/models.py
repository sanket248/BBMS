from django.db import models

# Create your models here.

class Donor(models.Model):
    donor_id = models.AutoField(primary_key=True, auto_created=True)
    donor_name = models.CharField(max_length=20)
    contect_no = models.CharField(max_length=10)
    blood_group = models.CharField(max_length=3)
    address = models.CharField(max_length=30)
    city = models.CharField(max_length=10)
    gender_choices=[
        ('male',"Male"),
        ("female","Female"),
    ]
    gender = models.CharField(
        max_length=6, blank=True, null=True,
        choices=gender_choices,
        )
    
    def __str__(self):
        return self.name