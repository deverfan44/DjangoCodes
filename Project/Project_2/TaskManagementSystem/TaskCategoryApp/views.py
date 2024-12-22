from django.shortcuts import render
from TaskCategoryApp.forms import categoryForm
# Create your views here.
def taskCategory(request):
    if request.method == 'POST':
        form = categoryForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save(commit=True)
    else:
        form = categoryForm()
    return render(request, './TaskCategoryApp/category.html', {'form':form})