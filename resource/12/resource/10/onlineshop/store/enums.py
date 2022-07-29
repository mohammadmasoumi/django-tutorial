from django.db import models


class MembershipChoices(models.TextChoices):
    BRONZE = 'B', 'Bronze'
    SILVER = 'S', 'Silver'
    GOLDEN = 'G', 'Golden'


class PaymentStatusChoices(models.TextChoices):
    PENDING = 'P', 'Pending'
    COMPLETE = 'C', 'Complete'
    FAILED = 'F', 'Failed'