from django.shortcuts import render, get_object_or_404

from practicums.models import Practicums
def index(request):
    return render(request, "main/index.html")

def products(request):
    return render(request, "main/products.html")

def club(request):
    return render(request, "main/club.html")

def practicums(request):

    practicums = Practicums.objects.all()

    context = {
        'practicums': practicums,
    }

    return render(request, "main/practicums.html", context)




