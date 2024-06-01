from django.shortcuts import render,redirect
from .forms import CategoryFrom

# Create your views here.

def AddCategory(request):
    if request.method =='POST':
        cate = CategoryFrom(request.POST)
        if cate.is_valid():
            cate.save()
            return redirect('addcategory')
    else:
        cate = CategoryFrom()
    return render(request,'category.html',{'form':cate})
