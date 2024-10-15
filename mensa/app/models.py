from django.db import models

class Mensa(models.Model):
    """
    Model for a mensa (cafeteria)
    All text fields are non-nullable but blankable
    """

    name = models.TextField(blank=True, null=False)
    address = models.TextField(blank=True, null=False)