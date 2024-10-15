from django.db import models


class Mensa(models.Model):
    """
    Model for a mensa (cafeteria)
    All text fields are non-nullable but blankable
    """

    class CampusLocation(models.TextChoices):
        ZENTRUM = "ZH", "Zentrum"
        HOENGGERBERG = "HB", "Hönggerberg"
        OERLINKON = "OK", "Oerlikon"
        BASEL = "BS", "Basel"

    name = models.TextField(blank=True, null=False)
    address = models.TextField(blank=True, null=False)
    campus_location = models.CharField(
        choices=CampusLocation, default=CampusLocation.ZENTRUM
    )
    # TODO: add opening hours


# class MealPlan(models.Model):
#     mensa = models.ForeignKey(null=True, on_delete=models.CASCADE)
#     date_from = models.DateField(null=False)
#     date_to = models.DateField(null=False)


class LunchMeal(models.Model):
    # class DayOfWeek(models.TextChoices):
    #     MONDAY = "MON", "Monday"
    #     TUESDAY = "TUE", "Tuesday"
    #     WEDNESDAY = "WED", "Wednesday"
    #     THURSDAY = "THU", "Thursday"
    #     FRIDAY = "FRI", "Friday"
    #     SATURDAY = "SAT", "Saturday"
    #     SUNDAY = "SUN", "Sunday"

    date = models.DateField(null=False)
    mensa = models.ForeignKey(Mensa, on_delete=models.CASCADE)


class EveningMeal(models.Model):
    date = models.DateField(null=False)
    mensa = models.ForeignKey(Mensa, on_delete=models.CASCADE)
