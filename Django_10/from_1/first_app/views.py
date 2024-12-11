from django.shortcuts import render
from . forms import contactForm

def home(request):
    return render(request, './first_app/home.html')

def about(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('Email',"Don't put email")
        district = request.POST.get('District')
        return render(request, './first_app/about.html', {'name': name, 'email': email, 'district': district})
    else:
        return render(request, './first_app/about.html')

def form(request):
    return render(request, './first_app/form.html')
        
def DjangoForm(request):
    form = contactForm(request.POST)
    if form.is_valid():
        print(form.cleaned_data)
    return render(request, './first_app/djangoForm.html', {'form': form})