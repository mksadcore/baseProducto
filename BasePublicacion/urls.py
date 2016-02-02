"""BasePublicacion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'vistaPublicar.views.base', name='base'),
    url(r'^servicios/', 'vistaPublicar.views.servicios', name='servicios'),
    url(r'^categorias/', 'vistaPublicar.views.categoria', name='categoria'),
    url(r'^productos/', 'vistaPublicar.views.productos', name='productos'),
    url(r'^casas/', 'vistaPublicar.views.casas', name='casas'),
    url(r'^departamentos/', 'vistaPublicar.views.departamentos', name='departamentos'),
    url(r'^locales/', 'vistaPublicar.views.locales', name='locales'),
    url(r'^naves/', 'vistaPublicar.views.navesIndustriales', name='naves'),
    url(r'^bodegas/', 'vistaPublicar.views.bodegas', name='badegas'),

]
