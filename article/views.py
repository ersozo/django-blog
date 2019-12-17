from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    # return HttpResponse("Ana Sayfa")
    return render(request, template_name="index.html")

def about(request):
    return render(request, "about.html")

