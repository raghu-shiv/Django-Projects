from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("This is the boy view.")

def paths(request):
    
    context = {
        'heading': "django tutorial 1",
        'content': "This is my learning phase."
    }

    return HttpResponse("This is the paths view.")