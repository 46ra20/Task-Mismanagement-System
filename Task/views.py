from django.shortcuts import render,redirect
from .forms import TaskForms
from .models import TaskModels
# Create your views here.
def AddTask(r):
    if r.method =='POST':
        auth = TaskForms(r.POST)
        if auth.is_valid():
            auth.save()
            auth=TaskForms()
            return redirect("showtask")
    else:
        auth=TaskForms()
    return render(r,'task.html',{'form':auth})

def getTask(request):
    data = TaskModels.objects.all()

    return render(request,'showTask.html',{'data':data})

def editTask(request,id):
    data  = TaskModels.objects.get(pk=id)
    p = TaskForms(instance=data)
    print(id)
    if request.method == 'POST':
        p=TaskForms(request.POST,instance=data)
        if p.is_valid():
            p.save()
            return redirect('showtask')
    return render(request,'task.html',{'form':p})

def deleteTask(requst,id):
    data = TaskModels.objects.get(pk=id)
    data.delete()
    return redirect('showtask')
