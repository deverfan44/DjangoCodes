from django.shortcuts import render
from . forms import userForm

def djangoForm(request):
    if request.method == "POST":
        form = userForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data) 
    else:
        form = userForm()

    return render(request, './djangoApp/django_form.html', {'form': form})