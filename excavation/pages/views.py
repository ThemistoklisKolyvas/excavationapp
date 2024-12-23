from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def base_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    #return HttpResponse("<h1>Hello World</h1>") #string of HTML code not actuall HTML 
   
    return render(request, "base.html", {})

# def contact_view(request, *args, **kwargs):
#     return HttpResponse("<h1>Contact Page<h1>")

# def about_view(request, *args, **kwargs):
#     return HttpResponse("<h1>About Page<h1>")