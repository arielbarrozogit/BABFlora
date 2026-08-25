from django.contrib import admin

from .models import (
    Collection,
    TaxonRank,
    TaxonNode,
    KeyNode,
    DecisionOption
)

admin.site.register(Collection)
admin.site.register(TaxonRank)
admin.site.register(TaxonNode)
admin.site.register(KeyNode)
admin.site.register(DecisionOption)
