from django.http import HttpResponse
from django.shortcuts import render, HttpResponse
from home.models import Contact

# Create your views here.
def home(request):
    # return HttpResponse("This is the home page.")
    # context = {'name': 'Shivendra', 'skills': 'Django, Python, HTML, CSS, Bootstrap'}
    # return render(request, 'index.html', context)
    return render(request, 'index.html')

def about(request):
    # return HttpResponse("This is the about page.")
    return render(request, 'about.html')

def contact(request):
    # return HttpResponse("This is the contact page.")
    if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']
        c = Contact(name=name, email=email, phone=phone, desc=desc)
        c.save()
        
    return render(request, 'contact.html')

def blog(request):
    # return HttpResponse("This is the blog page.")
    return render(request, 'blog.html')
