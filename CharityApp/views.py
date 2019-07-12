from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

from .models import Pet
from .models import MonthlyReport

def home(request):
    return render(request, 'home.html')

def help(request):
    return render(request, 'help.html')

def adoption(request):
    pets = Pet.objects.all()

    #return render()
    return render(request, 'adoption.html', {'pets': pets})

def pet_detail(request, id):
    try:
        pet = Pet.objects.get(id=id)
    except Pet.DoesNotExist:
        raise Http404('Pet not found')
    return render(request, 'pet_detail.html', {'pet': pet})

def reports(request):
    reports = MonthlyReport.objects.all()
    return render(request, 'reports.html', {'reports': reports})

def about(request):
    return render(request, 'about.html')