from django.shortcuts import render
from .models import ChaiType

# Create your views here.
def all_chai(request):
    chais = ChaiType.objects.all()
    return render(request,"chai/all_chai.html",{'chais':chais})