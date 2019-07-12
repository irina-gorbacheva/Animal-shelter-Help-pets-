from django.contrib import admin

from .models import Pet
from .models import Vaccine
from .models import MonthlyReport

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ['name', 'species', 'breed', 'sex', 'age']

@admin.register(Vaccine)
class VaccineAdmin(admin.ModelAdmin):
    pass

@admin.register(MonthlyReport)
class MonthlyReportAdmin(admin.ModelAdmin):
    list_display = ['month', 'year', 'pets_resqued', 'money_spent']
