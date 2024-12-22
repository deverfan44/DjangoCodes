from django.shortcuts import render,redirect
from TaskModelApp.forms import taskForm
from TaskModelApp.models import Task
# Create your views here.
def taskModel(request):
    if request.method == 'POST':
        form = taskForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save(commit=True)
    else:
        form = taskForm()
    return render(request, './TaskModelApp/task.html', {'form': form})

def edit_task(request, id):
    catch_form = Task.objects.get(pk=id)
    edit_form = taskForm(instance=catch_form)
    if request.method == 'POST':
        edit_form = taskForm(request.POST, instance=catch_form)
        if edit_form.is_valid():
            print(edit_form.cleaned_data)
            edit_form.save(commit=True)
        return redirect('home')
    return render(request, './TaskModelApp/task.html', {'form': edit_form})

def delete_task(request, id):
    delete_form = Task.objects.get(pk=id)
    delete_form.delete()
    return redirect('home')