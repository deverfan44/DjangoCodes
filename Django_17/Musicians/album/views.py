from django.shortcuts import render, redirect
from album.forms import albumFrom
from album.models import albumModel
# Create your views here.
def album(request):
    if request.method == 'POST':
        form = albumFrom(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            form.save(commit=True)
    else:
        form = albumFrom()
    return render(request, './album/album.html', {'form' : form})

def edit_album(request, id):
    catch_form = albumModel.objects.get(pk=id)
    new_edit = albumFrom(instance=catch_form)
    if request.method == 'POST':
        new_edit = albumFrom(request.POST, instance=catch_form)
        if new_edit.is_valid():
            new_edit.save(commit=True)
        return redirect('home')
    return render(request,'./album/album.html', {'form':new_edit})

def delete_album(request, id):
    catch_form = albumModel.objects.get(pk=id)
    catch_form.delete()
    return redirect('home')

