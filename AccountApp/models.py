from django.db import models
from django.contrib.auth.models import AbstractUser
import django.core.validators import MinLengthValidator,MaxLengthValidator,RegexValidator
from django.utils import timezone

# Create your models here.

class Speciality(models.Model):
    name=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeFiled(auto_now=True)
    

class User(AbstractUser):
    pass

class Doctor(User):
    licence_number = models.CharField(max_length=6,unique=True,validators=[MinLengthValidator(6)])
    phone=models.CharField(max_length=8)
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeFiled(auto_now=True)
    #specialities=models.ManyToManyField("AccountApp.Speciality",)
    specialities=models.ManyToManyField(
        Speciality,
        related_name="doctors"
    )
def validate_birth_date(v):
    if v>=timezone.localdate():
        raise ValidationError("La date de naissance doit etreinférirur à la date d'aujourd'hui")
class Patient(User):
    national_id=models.CharField(max_length=8,unique=True,validators=[RegexValidator(regex=r'^\d{8}$' , message="Le numero est incorrecte, ne respecte le pattern 8 chiffres exacte")])
    phone=models.CharField(max_length=8,validators=[number_validator])
    birth_date=models.DateField(validators=[validate_birth_date])
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeFiled(auto_now=True)

