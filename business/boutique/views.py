from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'boutique/home.html')
    
def index(request):
    return render(request, 'boutique/index.html')
    
    
def about(request):
    return render(request, 'boutique/about.html')

def sidebar(request):
    return render(request, 'boutique/sidebar-left.html')
    
def index2(request):
    return render(request, 'boutique/index2.html')