from django.db import models

SEXE = (
    ('homme', 'Homme'),
    ('femme', 'Femme'),
)

class Carte(models.Model):
    nom = models.CharField(max_length=100)
    postnom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    sexe = models.CharField(choices=SEXE, max_length=10)
    email = models.CharField(max_length=100)
    telephone = models.CharField(max_length=100)
    date_naissance = models.CharField(max_length=20)
    lieu_naissance = models.CharField(max_length=50)
    # photo = models.ImageField(upload_to='photo/')
    adresse = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.nom} {self.postnom} {self.prenom}'