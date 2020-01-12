from django.shortcuts import render

def home(request):
    context = {
        "title": "Home",
        "msg": "Hello World!",
    }
    return render(request, 'homepage.html', context)

# Create your views here.
