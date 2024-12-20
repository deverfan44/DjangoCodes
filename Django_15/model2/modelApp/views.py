from django.shortcuts import render
from modelApp.forms import StudentFrom


def home(request):
    if request.method == 'POST':
        form = StudentFrom(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print(form.cleaned_data)
    else:
        form = StudentFrom()
    return render(request, 'modelApp/home.html', {'form':form})

