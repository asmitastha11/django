from django.shortcuts import render, HttpResponse,redirect
from .models import Todolist
# Create your views here.
def home(request):
    return render(request,'home.html')


def task(request):
    tasks = Todolist.objects.all()
    total = tasks.count()
    completed = Todolist.objects.filter(is_completed = True).count()
    notcompleted = Todolist.objects.filter(is_completed = False).count()
    context = {
        "tasks" : tasks,
        "total" : total,
        "completed":completed,
        "notcompleted":notcompleted
    }
    return render(request,'task.html',context)

def task_create(request):
    if request.method == "POST":
        titles = request.POST.get('title')
        descriptions = request.POST.get('description')
        if titles == '' or descriptions == '':
            context = {
                'error':"Both fields required"
            }
            return render(request,'create.html',context)
        Todolist.objects.create(title=titles, description=descriptions)#tittle is from the form that we created and titles is variable
         # return HttpResponse(title)
        return redirect("/task/")
    return render(request,'create.html')
def mark_complete(request,pk):
    task = Todolist.objects.get(pk = pk)#pk-primary key
    task.is_completed = True
    task.save()
    return redirect('/task')
def mark_edit(request,pk):
    task = Todolist.objects.get(pk = pk)
    context = {"task":task}
    if request.method == "POST":
        titles = request.POST.get('title')
        descriptions = request.POST.get('description')
        if titles == '' or descriptions == '':
            context = {
                'error':"Both fields required"
            }
            return render(request,'edit.html',context)
        task.title = titles
        task.description = descriptions
        task.save()
        return redirect('/task')
    return render(request,'edit.html',context)

def mark_delete(request,pk):
    task = Todolist.objects.get(pk = pk)#pk-primary key  
    task.delete()
    return redirect('/task')