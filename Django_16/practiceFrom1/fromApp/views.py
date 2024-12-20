from django.shortcuts import render
from fromApp.forms import userFroms

# Create your views here.
def userFrom(request):
    if request.method == 'POST':
        create_form = userFroms(request.POST)
        if create_form.is_valid():
            print(create_form.cleaned_data)
    else:
        create_form = userFroms()
    return render(request,'./fromApp/form.html', {'form': create_form})