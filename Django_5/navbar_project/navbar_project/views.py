from django.shortcuts import render

def home(request):
    dic = {'name': 'Erfan', 'age': 23, 'list':[10,20,30,40]}
    return render(request,'index.html', context=dic)