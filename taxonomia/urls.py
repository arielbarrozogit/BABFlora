from django.urls import path

from .views import clave

from .views import(
    clave,
    familias,
    familia_detail,
    genus_detail,
    taxon_detail,
)


urlpatterns = [
    path(
        'clave/<int:node_id>/',
        clave,
        name='clave'
    ),
    path(
        'familias/',
        familias,
        name='familias'
    ),

    path(
        'familia/<int:id>/',
        familia_detail,
        name='familia_detail'
    ),
    path(
        'genero/<int:id>/',
        genus_detail,
        name='genus_detail'
    ), 
    path(
        'taxon/<int:id>/',
        taxon_detail,
        name='taxon_detail'
    )   
]