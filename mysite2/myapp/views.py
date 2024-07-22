from django.shortcuts import render,redirect
from .models import Task


def add(request):
    if request.method == 'POST':
        name = request.POST.get('name','')
        priority = request.POST.get('priority','')
        task = Task(name=name,priority=priority)
        task.save()

        return redirect('/')

    return render(request,'myapp/add.html')


def index(request):
    task_list = Task.objects.all()
    
    return render(request,'myapp/index.html',{'task_list':task_list})

# Create your views here.
