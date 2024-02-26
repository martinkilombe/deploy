from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import PortfolioItem

def home(request):
    items = PortfolioItem.objects.all()
    return render(request, 'portfolio/home.html', {'items': items})
