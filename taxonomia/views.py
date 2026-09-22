import re
from django.shortcuts import render
from django.urls import reverse
from .models import Family, Genus, Taxon, TaxonLink

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

    clave_html = familia.clave or ""

    for genero in generos:
       
        url = reverse(
            'genus_detail',
            args=[genero.id]
        )
        enlace = (
            f'<a href="{url}">'
            f'{genero.genus}'
            f'</a>'
        )
        patron = r'\b' + re.escape(genero.genus) + r'\b'
        clave_html = re.sub(
            patron,
            enlace,
            clave_html
        )

        familia.clave = clave_html

    return render(
        request,
        'taxonomia/familia_babflora.html',       {
            'familia': familia,
            'generos': generos,
           
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

    clave_html = genero.Claveidentif or ""

    for taxon in taxones:
        url = reverse(
            'taxon_detail',
            args=[taxon.id]
        )
        if getattr(taxon, 'subspecie', None):

            texto = (
                f"{genero.genus[0]}. "
                f"{taxon.specie}"
                f" ssp. {taxon.subspecie}"
            )

            enlace = (
                f'<a href="{url}">'
                f'{texto}'
                f'</a>'
            )
            clave_html = clave_html.replace(
                texto,
                enlace
                )


            #patron = r'\b' + re.escape(texto) + r'\b'

            clave_html = re.sub(
                patron,
                enlace,
                clave_html
            )

        #
    # PASADA 2
    # ESPECIES SIMPLES
    #
    for taxon in taxones:
        
        if getattr(taxon, 'subspecie', None):
            continue
        
        if getattr(taxon, 'variety', None):
            continue

        url = reverse(
        'taxon_detail',
        args=[taxon.id]
        )
        
        texto = (
        f"{genero.genus[0]}. "
        f"{taxon.specie}"
        )
        
        enlace = (
        f'<a href="{url}">'
        f'{texto}'
        f'</a>'
        )
        
        patron = r'\b' + re.escape(texto) + r'\b'
        
        clave_html = re.sub(
        patron,
        enlace,
        clave_html
        )



    genero.Claveidentif = clave_html

    return render(
        request,
        'taxonomia/genus_babflora.html',
        {
            'genero': genero,
            'taxones': taxones
        }
    )

def taxon_detail(request, id):

    taxon = Taxon.objects.using(
        'dbgermoherb_22082014'
    ).get(
        id=id
    )

    links = TaxonLink.objects.using(
        'dbgermoherb_22082014'
    ).filter(
        idTaxon=id
    )

    return render(
        request,
        'taxonomia/taxon_detail.html',
        {
            'taxon': taxon,
            'links': links
        }
    )


