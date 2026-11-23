from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator

class Appointment(models.Model):
    reason=models.TextField()
    prescription=models.FileField(
        blank=True,
        upload_to='prescription'
    )
    class Status(models.TextChoices):
        PENDING = "PENDING","En attente"
        CONFIRMED = "CONFIRMED","confirmé"
        CANCELLED = "CANCELLED","Annulé"
    status=models.CharField(max_length=10,choices=Status.choices,default=Status.PENDING)
    duration_minutes=models.PositiveIntegerField(default=30)
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    appointment_date=models.DateField()
    doctor=models.ForeignKey("AccountApp.Doctor",models.CASCADE,related_name="appointements")
    patient=models.ForeignKey("AccountApp.Patient",models.CASCADE,related_name="appointements")
    def clean(self):
        modified_date=self._state.adding or (
            Appointment.objects.filter(
                pk=self.pk,appointment_date=self.appointment_date
            ).exists()
        )
        if modified_date and self.appointment_date <= timezone.now():
            raise ValidationError("La date du rdv doit etre postérieur à la date")
        
    class Meta:
        ordering = ["appointment_date"]
        constraints = [
            models.UniqueConstraint(
                fields=["doctor", "appointment_date"],
                name="unicite-patient-doctor-date",
                violation_error_message="Ce docteur possède déjà un rendez-vous à cette date."
            )
        ]
def __str__(self):
    return f"le rdv est pour la raison {self.reason}"