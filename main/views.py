from django.shortcuts import render, get_object_or_404


from practicums.models import Practicums

from meditations.models import Meditation

from club.models import Schedule


from efiry.models import Efir

def index(request):
    return render(request, "main/index.html")

def products(request):
    return render(request, "main/products.html")

def oferta(request):
    return render(request, "oferta.html")



def practicums(request):

    practicums = Practicums.objects.all()

    context = {
        'practicums': practicums,
    }

    return render(request, "main/practicums.html", context)

def meditations(request):

    meditations = Meditation.objects.all()

    context = {
        'meditations': meditations,
    }

    return render(request, "main/meditations.html", context)

def club(request):

    schedule = Schedule.objects.all()

    context = {
        'schedule': schedule,
    }

    return render(request, "main/club.html", context)


def efiry(request):

    efiry = Efir.objects.all()

    context = {
        'efiry': efiry,
    }

    return render(request, "main/efiry.html", context)




