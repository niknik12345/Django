"""
URL configuration for trade project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from statistics import StatisticsError
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

#from tradesave import views

from tradesave.views import * 

urlpatterns = [
    path('admin', admin.site.urls),
    path('', index),#http://127.0.0.1:8000/index/
    path('user/', user),#http://127.0.0.1:8000/user/
    path('trade/', trade),#http://127.0.0.1:8000/trade/
    path('contact/', contact),#http://127.0.0.1:8000/contact/
    path('about/', about),#http://127.0.0.1:8000/about/

    #path("about/", TemplateView.as_view(template_name="about.html")),#http://127.0.0.1:8000/about/

    ############################################################
    path("indexbase", indexbase),#http://127.0.0.1:8000/indexbase/
    #path('indexbase/', indexbase, name='indexbase'),
    path("contactbase", contactbase),#http://127.0.0.1:8000/contactbase/
    path("aboutbase", aboutbase),#http://127.0.0.1:8000/aboutbase/
    path("tradebase", tradebase),#http://127.0.0.1:8000/tradebase/
    path("userbase", userbase),#http://127.0.0.1:8000/userbase/



    #path('admin/', admin.site.urls),
    #path('', include('tradesave.url')),#http://127.0.0.1:8000/index/
    #path('user/', user),#http://127.0.0.1:8000/user/
    #path('trade/', trade),#http://127.0.0.1:8000/trade/

]
from django.conf import settings
from django.conf.urls.static import static



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#if settings.DEBUG:
#    urlpatterns += StatisticsError(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

#hendler404 = pageNotFound
