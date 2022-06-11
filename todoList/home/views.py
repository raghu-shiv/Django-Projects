from sre_constants import SUCCESS
from django.shortcuts import render
from home.models import Task

# Create your views here.
def home(request):
    context = {'success': False, 'name': 'Shivendra'}
    if request.method=='POST':
      title=request.POST['title']
      desc=request.POST['desc']
      taskDetails=Task(title=title, desc=desc)
      taskDetails.save()
      context={'success' : True}

    return render(request, 'index.html', context)

def tasks(request):
  allTask=Task.objects.all()
  context={'tasks' : allTask}
  return render(request, 'tasks.html', context)
