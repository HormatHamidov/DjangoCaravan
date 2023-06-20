from django.shortcuts import render
# views.py
from .models import Meyve, Color


def meyve_view(request):
    name = request.GET.get('name')
    color = request.GET.get('color')
    
    meyveler = Meyve.objects.all()
    
    if name:
        meyveler = meyveler.filter(name__icontains=name)
    
    if color:
        meyveler = meyveler.filter(color__name=color)
    
    context = {
        'meyveler': meyveler,
        'colors': Color.objects.all()  # Tüm renkleri al
    }
    
    return render(request, 'meyve.html', context)
