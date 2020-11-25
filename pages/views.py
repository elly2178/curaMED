from django.shortcuts import render

def homepage_view(request,*args, **kwargs):
    return render(request, 'home.html',{})