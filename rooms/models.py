from django.db import models

# Create your models here.

from django.db import models

class Room(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Nombre de la habitación
    capacity = models.IntegerField()  # Capacidad máxima de la habitación
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)  # Precio por noche
    is_available = models.BooleanField(default=True)  # Disponibilidad

    def __str__(self):
        return self.name
