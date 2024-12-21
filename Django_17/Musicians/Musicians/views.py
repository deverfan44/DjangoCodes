from django.shortcuts import render
from musicianApp.models import musicianModel
from album.models import albumModel

def home(request):
    albumData = albumModel.objects.all()
    # print(musicianModel)
    return render(request, 'home.html', {'data':albumData})