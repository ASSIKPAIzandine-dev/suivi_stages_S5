from django.shortcuts import render
from stages.models import Entreprise


# Create your views here.
def liste_entreprises(request):
    return render(
        request,
        "stages/liste_entreprises.html",
        {"entreprises": Entreprise.objects.all()}
    )


def details_entreprises(request):
    pass


