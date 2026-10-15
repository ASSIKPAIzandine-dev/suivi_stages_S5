from django.shortcuts import get_object_or_404, render
from stages.models import Offre

def liste_offres(request):
    offres = Offre.objects.select_related("entreprise").prefetch_related("competences")
    return render(
        request,
        "stages/liste_offres.html",
        {"offres": offres},
    )

def detail_offre(request, pk):
    offre = get_object_or_404(
        Offre.objects.select_related("entreprise").prefetch_related("competences"),
        pk=pk,
    )
    return render(
        request,
        "stages/detail_offre.html",
        {"offre": offre},
    )



