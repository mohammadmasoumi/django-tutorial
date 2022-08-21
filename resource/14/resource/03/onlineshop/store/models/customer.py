from django.db import models
from store.enums import MembershipChoices 

"""
Bronze B
Silver S
Golden G
"""


class Customer(models.Model):
    # MEMBERSHIP_BRONZE = 'B'
    # MEMBERSHIP_SILVER = 'S'
    # MEMBERSHIP_GOLDEN = 'G'

    # MEMBERSHIP_CHOICES = [
    #     # 'B' actual value store in DB
    #     # 'Bronze' human readable in django admin
    #     (MEMBERSHIP_BRONZE, 'Bronze'),
    #     (MEMBERSHIP_SILVER, 'Silver'),
    #     (MEMBERSHIP_GOLDEN, 'Golden')
    # ]

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=11)
    membership = models.CharField(max_length=1, choices=MembershipChoices.choices, default=MembershipChoices.BRONZE)

    # membership = models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_BRONZE)

    # null=True/False
    # blank=True/False -> validation 
    # blank=False, null=False
    # https://docs.djangoproject.com/en/4.0/ref/models/fields/#null
    birth_date = models.DateField(null=True)
