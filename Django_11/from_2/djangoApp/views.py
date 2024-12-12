from django.shortcuts import render
from . forms import userForm

def djangoForm(request):
    if request.method == "POST":
        form = userForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data['upload']
            with open("./djangoApp/upload/"  + file.name, 'wb+') as destintaion:
                for chunck in file.chunks():
                    destintaion.write(chunck)
            print(form.cleaned_data) 
    else:
        form = userForm()

    return render(request, './djangoApp/django_form.html', {'form': form})