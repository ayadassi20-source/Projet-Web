from django.contrib import admin
from .models import Appointment
from AccountApp.models import Doctor
# Register your models here.
#admin.site.register(Appointment)

@admin.register(Appointment)
class AppointmentAdminPers(admin.ModelAdmin):
    #inlines=[DoctorPerso]
    list_display=('reason','status','duration_minutes','appointment_date')
    list_filter=('status','appointment_date')
    list_editable=('appointment_date','status')
    search_fields=('status','reason')
    list_per_page =2
    ordering=('-appointment_date',)
    fieldsets= (
        ('Description',{
            'fields': ('reason','status','prescription')
        }),
        ('Date + duration',{
            'fields':('appointment_date', 'duration_minutes')
        }),
        ('Patients/Doctors', {
            'fields' : ('patient','Doctor')
        }),
        ('planification', {
            'fields': ('created_at','update_at')
        }),
    )
    readonly_fields=('created_at','update_at')
#admin.site.register(Appointment,AppointmentAdminPers)