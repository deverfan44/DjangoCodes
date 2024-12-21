from django.shortcuts import render, redirect
from musicianApp.forms import musicianFrom
from musicianApp.models import musicianModel
# Create your views here.
def musician(request):
    if request.method == 'POST':
        form = musicianFrom(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save(commit=True)
    else:
        form = musicianFrom()
    return render(request, './musicianApp/musician.html', {'form':form})


def edit_musician(request, id):
    catchform = musicianModel.objects.get(pk=id)
    edit_form = musicianFrom(instance=catchform)
    if request.method == 'POST':
        edit_form = musicianFrom(request.POST, instance=catchform)
        if edit_form.is_valid():
            edit_form.save(commit=True)
        return redirect('home')
    return render(request, './musicianApp/musician.html', {'form':edit_form})
