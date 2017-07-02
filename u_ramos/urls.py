"""u_ramos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin

from core import models
from core.views import *

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', Home),
    url(r'^getdetails/', getdetails),
    url(r'^comentarios$', comentarios_ajax),
    url(r'^send_comm$', save_comm),
    url(r'^datos$', get_datos),
    url(r'^profesores/autocomplete/$', autocomplete, {'search_model': models.Profe},
        name='profe_autocomplete',
        ),
    url(r'^ramos/autocomplete/$', autocomplete, {'search_model': models.Ramo},
        name='ramo_autocomplete',
        ),

]