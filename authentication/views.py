from django.shortcuts import render

# Create your views here.


def auth(request):
    return render(request, 'authentication/auth.html')
