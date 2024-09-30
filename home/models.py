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
    telephone = models.CharField(max_length=100)
    date_naissance = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='photo/', blank=True)
    adresse = models.CharField(max_length=100)
    filiere = models.CharField(max_length=100, blank=True)
    promotion = models.CharField(max_length=100)
    
    email = models.CharField(max_length=100)
    lieu_naissance = models.CharField(max_length=50)

    annee_academique = models.CharField(max_length=100)
    nom_pere = models.CharField(max_length=100)
    contact_pere = models.CharField(max_length=100)
    nom_mere = models.CharField(max_length=100)
    contact_mere = models.CharField(max_length=100)
    nom_tuteur = models.CharField(max_length=100)
    contact_tuteur = models.CharField(max_length=100)

    nom_urgence = models.CharField(max_length=100)
    contact_urgence = models.CharField(max_length=100)

    date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.nom} {self.postnom} {self.prenom}'