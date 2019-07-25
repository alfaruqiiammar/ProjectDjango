<<<<<<< HEAD
from django.shortcuts import render,redirect, get_object_or_404
from .models import VocabsIndo, Artikel
from .filters import ArtikelFilter

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

def artikel_detail(request, blog_id):
    try:
        artikel = Artikel.objects.get(pk=blog_id)
    except Artikel.DoesNotExist:
        raise Http404('Artikel does not exist')
    return render(request, 'artikel_detail.html', {'artikel': artikel})

def headline(request):
    artikel = Artikel.objects.all()
    return render(request, 'headline.html', {'artikels': artikel})


def order3(request):
        # get the blog posts that are published
        artikel = Artikel.objects.order_by('-tanggal')[0:3]
        # now return the rendered template
        return render(request, 'home.html', {'artikels': artikel})

def artikel_kategori(request):
    f = ArtikelFilter(request.GET, queryset=Artikel.objects.all())
    return render(request, 'artikel_kategori.html', {'filter': f})

