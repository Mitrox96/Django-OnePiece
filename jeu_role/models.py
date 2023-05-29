from sys import maxsize
from xmlrpc.client import MAXINT
from django.db import models

# Create your models here.
CLASSE=(
    ('Soldat', 'Soldat'),
    ('Vice-Amiral', 'Vice-Amiral'),
    ('Amiral', 'Amiral'),
    ('Amiral en chef', 'Amiral en chef'),
    ('Simple pirate', 'Simple pirate'),
    ('Pirate important', 'Pirate important'),
    ('Grand corsaire', 'Grand corsaire'),
    ('Empereur', 'Empereur')
)

RACE=(
    ('Humain', 'Humain'),
    ('Homme-poisson', 'Homme-poisson'),
    ('Long-bras', 'Long-bras'),
    ('Minks', 'Minks'),
    ('Géant', 'Géant')
)


EQUIPEMENT=(
    ('Pyro-fruit', 'Pyro-fruit'),
    ('Fruit du GumGum', 'Fruit du GumGum'),
    ('Fruit du bistouri', 'Fruit du bistouri'),
    ('Grande lame', 'Grande lame'),
    ('Armure GERMA 66', 'Armure GERMA 66'),
    ('Arme antique', 'Arme antique')
)

class role(models.Model):
    nom = models.CharField(max_length=30)
    classe = models.CharField(max_length=20, choices=CLASSE)
    race = models.CharField(max_length=20, choices=RACE)
    niveau = models.PositiveIntegerField(default=1)
    equipement = models.CharField(max_length=20, choices=EQUIPEMENT)
    partie = models.PositiveIntegerField(default=1)
    def __str__(self):
        return "Nom : " + self.nom + "\nClasse : " + self.classe + "\nRace : " + self.race + "\nNiveau : " + str(self.niveau) + "\nEquipement : " + self.equipement + "\nNumero de partie : " + str(self.partie)


