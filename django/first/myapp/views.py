from django.shortcuts import render

def index(request):
    context = {
        'name':'Sho',
    }
    return render(request,'myapp/index2.html',context)

def about(request):
    return render(request,'myapp/about.html')

def info(request):
    return render(request,'myapp/info.html')
