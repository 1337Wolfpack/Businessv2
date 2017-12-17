from django.shortcuts import render
from django.template import Context
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

from django.http import HttpResponse
from django.template import loader
from .models import Product, ImageElement, Theme

#Index configurable 
def index(request):
    products = Product.objects.all()
    Banner = ImageElement.objects.get(nom="Banner")
    logo = ImageElement.objects.get(nom="logo")
    print(Banner.image.image.url)
    template = loader.get_template('boutique/cover.html')
    theme = Theme.objects.get(name="default")
    brand = theme.brand
    context = {
        'logo' : logo.image.image,
        'Banner' : Banner.image.image,
        'products': products,
        'brand' : brand,
        'theme' : theme,
    }
    return HttpResponse(template.render(context, request))



def dynamiccss(request):
    theme = Theme.objects.get(name="default")    
    template = loader.get_template('boutique/dynamiccss.css')
    context = {

        'theme' : theme,
    }
    return HttpResponse(template.render(context, request), content_type='text/css')



def home(request):
    return render(request, 'boutique/home.html')
    
    
def about(request):
    return render(request, 'boutique/about.html')

def sidebar(request):
    return render(request, 'boutique/sidebar-left.html')
    
def index2(request):
    return render(request, 'boutique/index2.html')
    