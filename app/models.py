from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator, MaxLengthValidator

# Create your models here.
class SexChoices(models.TextChoices):
    femenino = 'F', _('Femenino')
    masculino = 'M', _('Masculino')
    no_def = 'X', _('Prefiero no decir')

class RuidoChoices(models.TextChoices):
    alto = 'A', _('Bajo')
    medio = 'M', _('Medio')
    bajo = 'B', _('Alto')

class Medition(models.Model):
    # Identificación personal
    age = models.IntegerField(blank=False, default=18, validators=[MaxLengthValidator(2)])
    sex = models.CharField(choices=SexChoices.choices, blank=False, default=SexChoices.no_def)
    horas_audifonos = models.IntegerField(validators=[MaxValueValidator(24)])
    volume = models.CharField(choices=RuidoChoices.choices, blank=False, default=RuidoChoices.medio)
    noise_cancelation = models.BooleanField(blank=False, default=False)

    # Medición
    noise_value = models.IntegerField(
    validators=[MaxValueValidator(22000), MaxLengthValidator(5)], blank=False, default=20000)

    def __str__(self):
        return str(self.id)
    
    def __repr__(self):
        return self.age, self.sex, self.horas_audifonos, self.volume, self.noise_cancelation, self.noise_value