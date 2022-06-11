from django.shortcuts import render
from .models import Blog, Contact
import math

# Create your views here.
def home(request):
  return render(request, 'index.html')

def about(request):
  return render(request, 'about.html')

def contact(request):
  if request.method=="POST":
    name=request.POST['name']
    email=request.POST['email']
    phone=request.POST['phone']
    desc=request.POST['desc']
    ins=Contact(name=name, email=email, phone=phone, desc=desc)
    ins.save()
  return render(request, 'contact.html')

def blog(request):
  numOfPost = 4
  page=request.GET.get('page')
  if page is None:
    page=1
  else:
    page=int(page)
  
  '''
  page_1: 0 to 0 + numOfPost
  page_2: numOfPost to (numOfPost + numOfPost)
  page_3: (numOfPost + numOfPost) to (numOfPost + numOfPost + numOfPost)

  => (page-1)*numOfPost to page*numOfPost

  '''
  blogs=Blog.objects.all()
  length=len(blogs)
  blogs=blogs[(page-1)*numOfPost: page*numOfPost]
  if page>1:
    prev=page-1
  else:
    prev=None
  if page<math.ceil(length/numOfPost):
    nxt=page+1
  else:
    nxt=None
  context={'blogs':blogs, 'prev': prev, 'nxt':nxt}
  return render(request, 'blog.html', context)
  
def blogpost(request, slug):
  blog = Blog.objects.filter(slug=slug).first()
  context={'blog':blog}
  return render(request, 'blogpost.html', context)

def search(request):
  return render(request, 'search.html')
