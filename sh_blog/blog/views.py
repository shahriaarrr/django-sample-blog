from django.shortcuts import render, HttpResponse
from .forms import *
# Create your views here.
def home(request):
    return HttpResponse("<h1>Hello. welcome to shahriar's blog</h1>")

def Hi(request, name):
    return HttpResponse(f"<h1>Hello {name}</h1>")

def love(request, name, number):
    text = f"I love yo {name} :)</br>"
    count = 0
    while count != number:
        text += f"I love yo {name} :)</br>"
        count += 1

    return HttpResponse(text)

def signup(request):
    if request.method == "GET":
        form = SignUpForm()
        return render(request, 'signup.html', {'form' : form})
    elif request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
