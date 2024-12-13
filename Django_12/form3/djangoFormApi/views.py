from django.shortcuts import render
from . forms import submitFrom

def djangoform(request):
    if request.method == 'POST':
        form = submitFrom(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data['upload']
            with open('./djangoFormApi/upload/' + file.name , 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
            print(form.cleaned_data)
    else:
        form = submitFrom()
    return render(request,'./djangoFormApi/djangoform.html', {'form': form})
