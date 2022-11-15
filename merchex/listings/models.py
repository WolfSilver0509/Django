from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
"""
Les modèles sont des classes Python qui doivent remplir les critères suivants :
a) La classe doit hériter de models.Model.
b) Chaque attribut de la classe doit représenter un champ de modèle (un champ de modèle est une colonne dans une table de base de données).
c) Chaque attribut doit être une instance de Field (ou une de ses sous-classes).
d) Chaque attribut doit avoir un nom de champ de modèle (un nom de champ de modèle est le nom de la colonne dans la table de base de données).
e) Chaque attribut doit avoir un nom de champ de modèle unique.
f) Chaque attribut doit avoir un nom de champ de modèle qui ne contient pas d'espaces.
g) Chaque attribut doit avoir un nom de champ de modèle qui ne contient pas de caractères spéciaux.
h) Chaque attribut doit avoir un nom de champ de modèle qui ne commence pas par un soulignement.
i) Chaque attribut doit avoir un nom de champ de modèle qui ne soit pas un mot-clé réservé de Python.

charfield : https://docs.djangoproject.com/en/4.1/ref/models/fields/#django.db.models.CharField
le charfield est un champ de texte qui peut contenir jusqu'à 255 caractères.
commentaire rajout
"""
class Band(models.Model):

    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'


    name = models.fields.CharField(max_length=100)
    genre = models.fields.CharField(choices=Genre.choices, max_length=5)
    biography = models.fields.CharField(max_length=1000)
    year_formed = models.fields.IntegerField(
    validators=[MinValueValidator(1900), MaxValueValidator(2022)]
    )
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)


class Title(models.Model):
    title = models.fields.CharField(max_length=100)
