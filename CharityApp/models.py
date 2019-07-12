from django.db import models

class Pet(models.Model):
    CITY_CHOICES = [("Kh", "Kharkov"), ("Ki", "Kiev"), ("Od", "Odessa")]
    SEX_CHOICES = [("F", "Female"), ("M", "Male")]
    name = models.CharField(max_length = 100)
    species = models.CharField(max_length = 30)
    breed = models.CharField(max_length = 30, blank = True)
    sex = models.CharField(choices = SEX_CHOICES, max_length = 1)
    age = models.IntegerField(null = True)
    city = models.CharField(choices = CITY_CHOICES, max_length = 2)
    submission_date = models.DateTimeField()
    vaccinations = models.ManyToManyField('Vaccine', blank = True)

class Vaccine(models.Model):
    name = models.CharField(max_length = 50)

    def __str__(self):
        return self.name

class MonthlyReport(models.Model):
    month = models.CharField(max_length = 20)
    year = models.IntegerField()
    pets_resqued = models.IntegerField()
    money_spent = models.IntegerField()
    spends = models.TextField()

