from django.shortcuts import render
from categories.forms import CatagoryFrom

# Create your views here.
def add_category(request):
    if request.method == 'POST':
        catFrom = CatagoryFrom(request.POST)
        if catFrom.is_valid():
            catFrom.save(commit=True)
    else:
        catFrom = CatagoryFrom()
    return render(request, 'categories/category.html', {'form':catFrom})