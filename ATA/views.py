from django.shortcuts import render,redirect
from .models import VocabsIndo

# Create your views here.
def home(request):
    return render(request,'base/base.html')

def search(request):
    if request.method == 'GET':
        ini = request.GET.get('cari')
        if ini is not None:
            arti = VocabsIndo.objects.get(indo=ini)
            return render(request, 'searchkata.html', {'kata':ini,'arti': arti})
    return render(request,'search.html')

def coba(request):
    return render(request,'coba.html')
# def searchkata(request, kata):
#     if request.method == 'GET':
#         ini = request.GET.get('cari')
#         return render(request, 'searchkata.html', {'kata':ini})
#     return render(request, 'searchkata.html', {'kata': kata})
