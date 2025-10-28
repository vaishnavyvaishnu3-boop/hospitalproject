from django.shortcuts import render
from django.http import HttpResponse
from . models import patient_register,patient_appointment,medicalhistory,doctorschedule,eprescription,treatmentplan,facility,billing
from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User



def create_patient_register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        bloodgroup = request.POST.get('bloodgroup')
        height = request.POST.get('height')
        weight = request.POST.get('weight')
        qualification = request.POST.get('qualification')
        job = request.POST.get('job')
        income = request.POST.get('income')
        location = request.POST.get('location')
        Patient_register=patient_register(name=name,age=age,gender=gender,bloodgroup=bloodgroup,height=height,weight=weight,qualification=qualification,job=job,income=income,location=location)
        Patient_register.save()
        return redirect('aphomes')
    return render(request,'patientregistration.html')

def create_patient_appointment(request):
    if request.method == 'POST':
        names = request.POST.get('names')
        dob = request.POST.get('dob')
        phonenumber = request.POST.get('phonenumber')
        email = request.POST.get('email')
        date = request.POST.get('date')
        time = request.POST.get('time')
        reason = request.POST.get('reason')
        Patient_appointment=patient_appointment(names=names,dob=dob,phonenumber=phonenumber,email=email,date=date,time=time,reason=reason)
        Patient_appointment.save()
        return redirect('aadmhomes')
    return render(request,'appointmentform.html')


def list_patient_appointment(request):
    Patient_appointments = patient_appointment.objects.all()
    return render(request,'eachappointmentform.html',{'Patient_appointments':Patient_appointments})

def each_patient_appointment(request,Patient_appointment_id):

    Patient_appointment=patient_appointment.objects.get(id=Patient_appointment_id)
    return render(request,'detailappointmentform.html',{'Patient_appointment':Patient_appointment})

def update_patient_appointment(request,Patient_appointment_id):
    Patient_appointment=patient_appointment.objects.get(id=Patient_appointment_id)
    if request.method=='POST':
        names = request.POST.get('names')
        dob = request.POST.get('dob')
        phonenumber = request.POST.get('phonenumber')
        email = request.POST.get('email')
        date = request.POST.get('date')
        time = request.POST.get('time')
        reason = request.POST.get('reason')

        Patient_appointment.names=names
        Patient_appointment.dob=dob
        Patient_appointment.phonenumber=phonenumber
        Patient_appointment.email=email
        Patient_appointment.date=date
        Patient_appointment.time=time
        Patient_appointment.reason=reason
        Patient_appointment.save()
        return redirect('aadmhomes')
    return render(request,'updateappointmentform.html',{'Patient_appointment':Patient_appointment})

def delete_patient_appointment(request,Patient_appointment_id):
    Patient_appointment=patient_appointment.objects.get(id=Patient_appointment_id)
    if request.method=='POST':
        Patient_appointment.delete()
        return redirect('aadhomes')
    return render(request,'cancelappointmentform.html',{'Patient_appointment':Patient_appointment})

def create_medicalhistory(request):
    if request.method =='POST':
        named = request.POST.get('named')
        address = request.POST.get('address')
        dateofbirth = request.POST.get('dateofbirth')
        genders = request.POST.get('genders')
        contactnumber = request.POST.get('contactnumber')
        mail = request.POST.get('mail')
        allergy = request.POST.get('allergy')
        medication = request.POST.get('medication')
        chronic = request.POST.get('chronic')
        surgery = request.POST.get('surgery')
        history = request.POST.get('history')
        comment = request.POST.get('comment')
        Medicalhistory=medicalhistory(named=named,address=address,dateofbirth=dateofbirth,genders=genders,contactnumber=contactnumber,mail=mail,allergy=allergy,medication=medication,chronic=chronic,surgery=surgery,history=history,comment=comment)
        Medicalhistory.save()
        return redirect('aphomes')
    return render(request,'medicalhistoryform.html')

def list_medicalhistory(request):
    Medicalhistories = medicalhistory.objects.all()
    return render(request,'listmedicalhistoryform.html',{'Medicalhistories':Medicalhistories})


def create_doctorschedule(request):
    if request.method == 'POST':
        doctor = request.POST.get('doctor')
        times = request.POST.get('times')
        plana = request.POST.get('plana')
        planb = request.POST.get('planb')
        planc = request.POST.get('planc')
        pland = request.POST.get('pland')
        plane = request.POST.get('plane')
        Doctorschedule = doctorschedule(doctor=doctor,times=times,plana=plana,planb=planb,planc=planc,pland=pland,plane=plane)
        Doctorschedule.save()
        return redirect('adhomes')
    return render(request,'doctorscheduleform.html')


def list_doctorschedule(request):
    Doctorschedules = doctorschedule.objects.all()
    return render(request,'listdoctorscheduleform.html',{'Doctorschedules':Doctorschedules})

def create_eprescription(request):
    if request.method == 'POST':
        patient = request.POST.get('patient')
        ages = request.POST.get('ages')
        medications = request.POST.get('medications')
        dosage = request.POST.get('dosage')
        frequency = request.POST.get('frequency')
        duration = request.POST.get('duration')
        dated = request.POST.get('dated')
        Eprescription = eprescription(patient=patient,ages=ages,medications=medications,dosage=dosage,frequency=frequency,duration=duration,dated=dated)
        Eprescription.save()
        return redirect('adhomes')
    return render(request,'electronicprescriptionform.html')

def list_eprescription(request):
    Eprescriptions = eprescription.objects.all()
    return render(request,'listelectronicprescriptionform.html',{'Eprescriptions':Eprescriptions})

def create_treatmentplan(request):
    if request.method == 'POST':
        naming = request.POST.get('naming')
        diagnosis = request.POST.get('diagnosis')
        problem = request.POST.get('problem')
        goals = request.POST.get('goals')
        objectives = request.POST.get('objectives')
        strategy = request.POST.get('strategy')
        modality = request.POST.get('modality')
        frequencies = request.POST.get('frequencies')
        estimate = request.POST.get('estimate')
        Treatmentplan = treatmentplan(naming=naming,diagnosis=diagnosis,problem=problem,goals=goals,objectives=objectives,strategy=strategy,modality=modality,frequencies=frequencies,estimate=estimate)
        Treatmentplan.save()
        return redirect('adhomes')
    return render(request,'treatmentplan.html')

def create_facility(request):
    if request.method == 'POST':
        strategies = request.POST.get('strategies')
        objective = request.POST.get('objective')
        actionl = request.POST.get('actionl')
        actionh = request.POST.get('actionh')
        actionr = request.POST.get('actionr')
        planl = request.POST.get('planl')
        planr = request.POST.get('planr')
        planh = request.POST.get('planh')
        Facility = facility(strategies=strategies,objective=objective,actionl=actionl,actionh=actionh,actionr=actionr,planl=planl,planr=planr,planh=planh)
        Facility.save()
        return redirect('aadmhomes')
    return render(request,'facilitymanagementform.html')

def list_facility(request):
    Facilities = facility.objects.all()
    return render(request,'listfacilitymanagement.html',{'Facilities':Facilities})

def list_treatmentplan(request):
    Treatmentplans = treatmentplan.objects.all()
    return render(request,'listtreatmentplan.html',{'Treatmentplans':Treatmentplans})

def create_billing(request):
    if request.method == 'POST':
        billnumber = request.POST.get('billnumber')
        dateds = request.POST.get('dateds')
        patientid = request.POST.get('patientid')
        patientname = request.POST.get('patientname')
        patientage = request.POST.get('patientage')
        patientgender = request.POST.get('patientgender')
        admissiondate = request.POST.get('admissiondate')
        dischargedate = request.POST.get('dischargedate')
        roomcharge = request.POST.get('roomcharge')
        doctorfee = request.POST.get('doctorfee')
        pathology = request.POST.get('pathology')
        misc = request.POST.get('misc')
        total = request.POST.get('total')
        Billing = billing(billnumber=billnumber,dateds=dateds,patientid=patientid,patientname=patientname,patientage=patientage,patientgender=patientgender,admissiondate=admissiondate,dischargedate=dischargedate,roomcharge=roomcharge,doctorfee=doctorfee,pathology=pathology,misc=misc,total=total)
        Billing.save()
        return redirect('aadmhomes')
    return render(request,'patientbillingform.html')

def registration_patient(request):
    if request.method=='POST':
        username=request.POST.get('username')
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'this username already exists')
                return redirect('registered')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'This email is already taken')
                return redirect('registered')
            else:
                user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
                user.save()
                return redirect('logged')
        else:
            messages.info(request,'This password is not matching')
            return redirect('registered')
    return render(request,'registerpatient.html')


def loginpatient(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=auth.authenticate(request, username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('seconds')
        else:
            messages.error(request,'Invalid username or password')
            return redirect('logged')



    return render(request,'loginpatient.html')

def home(request):
    return render(request,'home.html')

def patienthome(request):
    return render(request,'patienthome.html')

def doctorhome(request):
    return render(request,'doctorhome.html')

def administratorhome(request):
    return render(request,'administratorhome.html')