from django.shortcuts import render
from .models import Family, Genus, Taxon

# Create your views here.
from django.shortcuts import render, get_object_or_404

from .models import KeyNode


def clave(request, node_id):

    nodo = get_object_or_404(
        KeyNode,
        id=node_id
    )

    return render(
        request,
        "taxonomia/clave.html",
        {
            "nodo": nodo
        }
    )
def familias(request):

    familias = Family.objects.using(
    'dbgermoherb_22082014'
).all().order_by(
    'family_name'
)
    return render(
        request,
        'taxonomia/familias.html',
        {
            'familias': familias
        }
    )
def familia_detail(request, id):

    familia = Family.objects.using(
        'dbgermoherb_22082014'
    ).get(
        id=id
    )
    generos = Genus.objects.using(
        'dbgermoherb_22082014'
    ).filter(
        id_family=id
    ).order_by(
        'genus'
    )

    return render(
        request,
        'taxonomia/familia_babflora.html',
        {
            'familia': familia,
            'generos': generos
        }
    )

def genus_detail(request, id):

    genero = Genus.objects.using(
        'dbgermoherb_22082014'
    ).get(
        id=id
    )

    taxones = Taxon.objects.using(
        'dbgermoherb_22082014'
    ).filter(
        id_genus=id
    ).order_by(
        'specie'
    )

    return render(
        request,
        'taxonomia/genus_babflora.html',
        {
            'genero': genero,
            'taxones': taxones
        }
    )



