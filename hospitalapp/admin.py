from django.contrib import admin
from . models import patient_register,patient_appointment,medicalhistory,doctorschedule,eprescription,treatmentplan,facility,billing

admin.site.register(patient_register)
admin.site.register(patient_appointment)
admin.site.register(medicalhistory)
admin.site.register(doctorschedule)
admin.site.register(eprescription)
admin.site.register(treatmentplan)
admin.site.register(facility)
admin.site.register(billing)



