from django.shortcuts import render

# Create your views here.

# index
def index(request):
    datas = {
        
    }
    return render(request,  "index.html", datas)

# about
def about(request):
    datas = {
        
    }
    return render(request,  "about.html", datas)

# blog
def blog(request):
    datas = {
        
    }
    return render(request,  "blog.html", datas)

# contact
def contact(request):
    datas = {
        
    }
    return render(request,  "contact.html", datas)

# gallery
def gallery(request):
    datas = {
        
    }
    return render(request,  "gallery.html", datas)

# single
def single(request):
    datas = {
        
    }
    return render(request,  "blog-single.html", datas)

# services
def services(request):
    datas = {
        
    }
    return render(request,  "services.html", datas)
