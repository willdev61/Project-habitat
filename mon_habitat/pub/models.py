from django.db import models
from django.core.files.storage import FileSystemStorage

CITIES_CHOICES = [
    ('ABOBO', 'Abobo'),
    ('ADJAME', 'Adjamé'),
    ('ATTECOUBE', 'Attécoubé'),
    ('COCOCDY', 'Cocody'),
    ('KOUMASSI', 'Koumassi'),
    ('MARCORY', 'Marcory'),
    ('PLATEAU', 'Plateau'),
    ('PORT-BOUET', 'Port-Boùet'),
    ('TREICHVILLE', 'Treichville'),
    ('YOPOUGON', 'Yopougon'),
    ]
CATEGORIES_CHOICES = [
    ('VILLA', 'Villa'),
    ('APPARTEMENT', 'Appartement'),
    ('HAUT-STANDING', 'Haut-standing'),
    ('DUPLEX', 'Duplex'),
    ('COUR', 'Cour'),
    ('2 PIECES', '2 pièces'),
    ('3 PIECES', '3 pièces'),
    ]
STATUS_CHOICES = [
    ('VENTE', 'Vente'),
    ('LOCATION', 'Location'),
]
class Publication(models.Model):
    made_at = models.DateTimeField( auto_now_add=True)
    first_name = models.CharField('Nom', max_length=200)
    last_name = models.CharField('Prénoms', max_length=200)
    agency_name = models.CharField("Nom de l'agence", max_length=200)
    cities = models.CharField('Commune', max_length=200, choices=CITIES_CHOICES, unique=True)
    categories = models.CharField('Catégories', max_length=200, choices=CATEGORIES_CHOICES, unique=True)
    status = models.CharField('Statut', max_length=200, choices=STATUS_CHOICES, unique=True)
    number_1 = models.IntegerField('Contact 1')
    number_2 = models.IntegerField('Contact 2', null=True)
    description = models.TextField('Description', max_length=1000)
    image_one = models.FileField('Image', upload_to = 'img_upload/')