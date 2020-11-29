from django.db import models

# Create your models here.


class House(models.Model):

    apartment = 'apartment'
    mansion = 'mansion'
    villa = 'villa'
    small_house = 'small house'
    unknown = 'unknown'

    house_type = [
        (apartment, 'Apartment'),
        (mansion, 'Mansion'),
        (villa, 'Villa'),
        (small_house, 'Small House'),
        (unknown, 'Unknown'),
    ]

    type = models.CharField(max_length=30, choices=house_type, default=unknown)
    name = models.CharField(max_length=30, blank=False)
    size = models.IntegerField(blank=False)
    description = models.TextField(blank=False)
    owner_name = models.CharField(max_length=40, blank=False)
    image = models.ImageField(
        upload_to='houses'
    )

    # user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

