from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'homeapp/home.html')

def about(request):
    return render(request,'homeapp/about.html')