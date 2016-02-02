from django.shortcuts import render, get_object_or_404
from .models import Casas, Departamentos, Locales, Bodega
from .forms import casasForm
from .forms import departamentosForm
from .forms import navesIndustrialesForm
from .forms import localesForm
from .forms import bodegaForm
from django.http import HttpResponseRedirect


# Create your views here.

def base(request):
    return render(request,'base.html')

def categoria(request):
    return render(request,'categoria1.html')

def servicios(request):
    return render(request, 'Categorias/servicios.html')

def productos(request):

    return render(request, 'productos y otros.html')

def casas(request):
    if request.method == 'POST':
      form = casasForm(request.POST, request.FILES)
      if form.is_valid():
          post = form.save(commit=False)
          post.save()

          return HttpResponseRedirect('/casas/')
    else:
        form = casasForm()
    return render(request, 'Categorias/casas.html', {'form':form})


def departamentos(request):
    if request.method == 'POST':
      form = departamentosForm(request.POST, request.FILES)
      if form.is_valid():
          post = form.save(commit=False)
          post.save()

          return HttpResponseRedirect('/departamentos/')
    else:
        form = departamentosForm()
    return render(request, 'Categorias/departamento.html', {'form':form})


def locales(request):
    if request.method == 'POST':
      form = localesForm(request.POST, request.FILES)
      if form.is_valid():
          post = form.save(commit=False)
          post.save()

          return HttpResponseRedirect('/locales/')
    else:
        form = localesForm()
    return render(request, 'Categorias/locales.html', {'form':form})

def navesIndustriales(request):
    if request.method == 'POST':
      form = navesIndustrialesForm(request.POST, request.FILES)
      if form.is_valid():
          post = form.save(commit=False)
          post.save()

          return HttpResponseRedirect('/naves/')
    else:
        form = navesIndustrialesForm()
    return render(request, 'Categorias/nave_industriales.html', {'form':form})

def bodegas(request):
    if request.method == 'POST':
      form = navesIndustrialesForm(request.POST, request.FILES)
      if form.is_valid():
          post = form.save(commit=False)
          post.save()

          return HttpResponseRedirect('/bodegas/')
    else:
        form = navesIndustrialesForm()
    return render(request, 'Categorias/bodegas.html', {'form':form})