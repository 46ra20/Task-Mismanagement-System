from django.shortcuts import render

def HomePage(r):
    return render(r,'base.html')