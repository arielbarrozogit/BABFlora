from django.db import models


# ==========================
# RANGOS TAXONOMICOS
# ==========================

class TaxonRank(models.Model):

    nombre = models.CharField(
        max_length=50,
        unique=True
    )

    orden = models.IntegerField()

    class Meta:
        ordering = ['orden']

    def __str__(self):
        return self.nombre


# ==========================
# COLECCIONES
# ==========================

class Collection(models.Model):

    nombre = models.CharField(
        max_length=255
    )

    descripcion = models.TextField(
        blank=True
    )

    def __str__(self):
        return self.nombre


# ==========================
# NODO TAXONOMICO
# ==========================

class TaxonNode(models.Model):

    collection = models.ForeignKey(
        Collection,
        on_delete=models.CASCADE
    )

    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )

    rank = models.ForeignKey(
        TaxonRank,
        on_delete=models.PROTECT
    )

    scientific_name = models.CharField(
        max_length=255
    )

    author = models.CharField(
        max_length=255,
        blank=True
    )

    def __str__(self):
        return self.scientific_name


# ==========================
# CLAVES DICOTOMICAS
# ==========================

class KeyNode(models.Model):

    pregunta = models.TextField()

    def __str__(self):
        return self.pregunta


# ==========================
# OPCIONES DE DECISION
# ==========================

class DecisionOption(models.Model):

    key_node = models.ForeignKey(
        KeyNode,
        on_delete=models.CASCADE,
        related_name='opciones'
    )

    opcion = models.CharField(
        max_length=255
    )

    siguiente_nodo = models.ForeignKey(
        KeyNode,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='anteriores'
    )

    resultado_taxon = models.ForeignKey(
        TaxonNode,
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )

    def __str__(self):
        return self.opcion

class Family(models.Model):

    idGBCollection = models.IntegerField()

    family_name = models.CharField(
        max_length=20,
        null=True,
        blank=True
    )

    family_description = models.TextField(
        null=True,
        blank=True
    )

    referenciaBibliografica = models.TextField(
        null=True,
        blank=True
    )

    clave = models.TextField(
        null=True,
        blank=True
    )

    class Meta:
        managed = False
        db_table = 'tb_family'

class Genus(models.Model):

    idGBCollection = models.IntegerField()

    id_family = models.IntegerField(
        null=True,
        blank=True
    )

    genus = models.CharField(
        max_length=64,
        null=True,
        blank=True
    )

    autor = models.CharField(
        max_length=1024,
        null=True,
        blank=True
    )

    RefBibliografica = models.TextField(
        null=True,
        blank=True
    )

    Claveidentif = models.TextField(
        null=True,
        blank=True
    )

    Descripcion = models.TextField(
        null=True,
        blank=True
    )

    class Meta:
        managed = False
        db_table = 'tb_genus'
class Taxon(models.Model):

    idGBCollection = models.IntegerField(
        null=True,
        blank=True
    )

    id_family = models.IntegerField(
        null=True,
        blank=True
    )

    family = models.CharField(
        max_length=64,
        null=True,
        blank=True
    )

    genus = models.CharField(
        max_length=64,
        null=True,
        blank=True
    )

    id_genus = models.IntegerField(
        null=True,
        blank=True
    )

    specie = models.CharField(
        max_length=64,
        null=True,
        blank=True
    )
    subspecie = models.CharField(
        max_length=64,
        null=True,
        blank=True
        )

    variety = models.CharField(
    max_length=64,
    null=True,
    blank=True
    )
    

    ScientificName = models.CharField(
        max_length=150,
        null=True,
        blank=True
    )

    Claveidentif = models.TextField(
        null=True,
        blank=True
    )

    Descripcion = models.TextField(
        null=True,
        blank=True
    )

    class Meta:
        managed = False
        db_table = 'tb_taxon'

class TaxonLink(models.Model):

    idGBCollections = models.IntegerField()

    idTaxon = models.IntegerField()

    description = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    descriptionEng = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    pathThumbnail = models.CharField(
        max_length=512,
        null=True,
        blank=True
    )

    pathLink = models.CharField(
        max_length=512,
        null=True,
        blank=True
    )

    pathLinkUrl = models.CharField(
        max_length=512,
        null=True,
        blank=True
    )

    class Meta:
        managed = False
        db_table = 'tb_taxonlink'