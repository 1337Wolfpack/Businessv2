from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home', views.home, name='home/'),
    url(r'^about', views.about, name='boutique/'),
    url(r'^sidebar', views.sidebar, name='boutique/'),
    url(r'^index2', views.index2, name='boutique/'),
    url(r'^dynamiccss', views.dynamiccss, name='dynamiccss/'),
    url(r'^$', views.index, name='boutique/'),
  
]