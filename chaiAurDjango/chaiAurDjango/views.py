from django.http import HttpResponse

def home(request):
    return HttpResponse("You are in chai aur django home page")

def about(request):
    return HttpResponse("You are in chai aur django about page")

def contact(request):
    return HttpResponse("You are in chai aur django contact page") 