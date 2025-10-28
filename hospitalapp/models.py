from django.db import models

class patient_register(models.Model):
    name = models.CharField(max_length=100)
    age  = models.IntegerField()
    gender = models.CharField(max_length=100)
    bloodgroup = models.CharField(max_length=100)
    height = models.IntegerField()
    weight = models.IntegerField()
    qualification = models.CharField(max_length=100)
    job = models.CharField(max_length=100)
    income = models.IntegerField()
    location = models.CharField(max_length=200)

    def __str__(self):
        return '{}'.format(self.name)


class patient_appointment(models.Model):
    names = models.CharField(max_length=100)
    dob = models.DateField()
    phonenumber = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    date = models.DateField()
    time = models.CharField(max_length=200)
    reason = models.TextField(max_length=10000)

    def __str__(self):
        return '{}'.format(self.names)

class medicalhistory(models.Model):
    named = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    dateofbirth = models.DateField()
    genders = models.CharField(max_length=200)
    contactnumber =models.IntegerField()
    mail = models.EmailField()
    allergy = models.TextField(max_length=10000)
    medication = models.TextField(max_length=10000)
    chronic = models.TextField(max_length=10000)
    surgery = models.TextField(max_length=10000)
    history = models.TextField(max_length=10000)
    comment = models.TextField(max_length=10000)

    def __str__(self):
        return '{}'.format(self.named)

class doctorschedule(models.Model):
    doctor = models.CharField(max_length=100)
    times = models.CharField(max_length=100)
    plana = models.CharField(max_length=100)
    planb = models.CharField(max_length=100)
    planc = models.CharField(max_length=100)
    pland = models.CharField(max_length=100)
    plane = models.CharField(max_length=100)

    def __str__(self):
        return '{}'.format(self.doctor)

class eprescription(models.Model):
    patient = models.CharField(max_length=100)
    ages = models.IntegerField()
    medications = models.CharField(max_length=100)
    dosage = models.CharField(max_length=100)
    frequency = models.CharField(max_length=200)
    duration = models.CharField(max_length=200)
    dated = models.CharField(max_length=200,default='')

    def __str__(self):
        return '{}'.format(self.patient)

class treatmentplan(models.Model):
    naming = models.CharField(max_length=100)
    diagnosis = models.CharField(max_length=100)
    problem = models.CharField(max_length=200)
    goals = models.CharField(max_length=100)
    objectives = models.CharField(max_length=200)
    strategy = models.CharField(max_length=100)
    modality = models.CharField(max_length=100)
    frequencies = models.CharField(max_length=200)
    estimate = models.CharField(max_length=200)

    def __str__(self):
        return '{}'.format(self.naming)

class facility(models.Model):
    strategies = models.TextField()
    objective = models.TextField()
    actionl = models.TextField()
    actionh = models.TextField()
    actionr = models.TextField()
    planl = models.TextField()
    planr = models.TextField()
    planh = models.TextField()

    def __str__(self):
        return '{}'.format(self.strategies)

class billing(models.Model):
    billnumber = models.IntegerField()
    dateds = models.DateField()
    patientid = models.IntegerField()
    patientname = models.CharField(max_length=100)
    patientage = models.IntegerField()
    patientgender = models.CharField(max_length=100)
    admissiondate = models.DateField()
    dischargedate = models.DateField()
    roomcharge = models.IntegerField()
    doctorfee = models.IntegerField()
    pathology = models.IntegerField()
    misc = models.IntegerField()
    total = models.IntegerField()

    def __str__(self):
        return '{}'.format(self.billnumber)



