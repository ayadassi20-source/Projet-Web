from django.db import models
from AccountApp.models import Doctor
# Create your models here.
class Appointment(models.Model):
    reason=models.TextField()
    prescription=models.FileField(
        blank=True,
        upload_to='prescriptions/'
    )
    class Status(models.TextChoices):
        PENDING = "PENDING","En attente"
        CONFIRMED = "CONFIRMED", "Confirmé"
        CANCELLED = "CANCELLED", "Annulé"
    status= models.CharField(max_length=10,choices=Status.choices,default=Status.PENDING)
    duration_minutes = models.PositiveIntegerField(default=30)
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeFiled(auto_now=True)
    appointment_date=models.DateField()
    doctor=models.Foreignkey(Doctor,on_delete=models.CASCADE,related_name="appointments")
    patient=models.Foreignkey("AccountApp.Patient",on_delete=models.CASCADE,related_names="appointments")
    class Meta:
        constraints= [
            models.UniqueConstraints(
                fields=["doctor","appointment_date"]
                name="unicite_patient-doctor-date",
                violation_error_message="ce docteur possede un rdv avec cette date"
            )
        ]