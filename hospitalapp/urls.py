from django.urls import path
from . import views


urlpatterns = [
    path("crea/",views.create_patient_register,name="acrea"),
    path("created/",views.create_patient_appointment,name='acreated'),
    path('listed/',views.list_patient_appointment,name='alisted'),
    path('detail/<int:Patient_appointment_id>/',views.each_patient_appointment,name="adetail"),
    path('update/<int:Patient_appointment_id>/',views.update_patient_appointment,name="aupdate"),
    path('delete/<int:Patient_appointment_id>/',views.delete_patient_appointment,name="adelete"),
    path('creating/',views.create_medicalhistory,name="acreating"),
    path('listing/',views.list_medicalhistory,name="alisting"),
    path('creatings/',views.create_doctorschedule,name="acreatings"),
    path('detailed/',views.list_doctorschedule,name="adetailed"),
    path('creation/',views.create_eprescription,name="acreation"),
    path('detailing/',views.list_eprescription,name="adetailing"),
    path('creatic/',views.create_treatmentplan,name="acreatic"),
    path('creatin/',views.create_facility,name="acreatin"),
    path('listings/',views.list_facility,name="alistings"),
    path('listeds/',views.list_treatmentplan,name="alisteds"),
    path('creatig/',views.create_billing,name="acreatig"),
    path('registered/',views.registration_patient,name="aregistered"),
    path('logged/',views.loginpatient,name="alogged"),
    path('homes/',views.home,name="ahomes"),
    path('phomes/',views.patienthome,name="aphomes"),
    path('dhomes/',views.doctorhome,name="adhomes"),
    path('admhomes/',views.administratorhome,name="aadmhomes")

]