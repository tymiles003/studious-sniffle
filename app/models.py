from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=600, blank=True)

    def __str__(self):
        return '{0}'.format(self.title)


class Person(models.Model):
    CAPABILITY_CHOICES = (
        ('ADS', 'ADS'),
        ('CDS', 'CDS'),
        ('VDS', 'VDS'),
        ('PCC', 'PCC'),
        ('VM', 'Virtualization'),
        ('AD', 'Active Directory'),
        ('BAC', 'Backup'),
        ('STO', 'Storage'),
        ('UNX', 'UNIX'),
        ('WIN', 'Wintel'))
    TEAM_CHOICES = (
        ('iACTION', 'iACTION'),
        ('iBUILD', 'iBUILD'),
        ('iENHANCE', 'iENHANCE'),
        ('iSOLVE', 'iSOLVE'))
    EMPLOY_CHOICES = (
        ('Contractor', 'Contractor'),
        ('Employee', 'Employee'))

    firstname = models.CharField(max_length=200, verbose_name='First name')
    lastname = models.CharField(max_length=200, verbose_name='Last name')
    shortname = models.CharField(max_length=200, unique=True, verbose_name='CSC shortname')
    startdate = models.DateField(auto_now_add=False, verbose_name='Start date')
    addeddate = models.DateTimeField(auto_now_add=True, verbose_name='Date added to status app')

    personalstreet = models.CharField(max_length=50, blank=True, verbose_name='Home street address')
    personalcity = models.CharField(max_length=50, verbose_name='Home city', default='Hartford')
    personalstate = models.CharField(max_length=50, verbose_name='Home state', default='CT')
    personalzip = models.CharField(max_length=5, blank=True, verbose_name='Home zip code')
    personalemail = models.EmailField(max_length=50, blank=True, verbose_name='Personal email address')
    personalphone = PhoneNumberField(blank=True, verbose_name='Personal phone number')

    workphone = PhoneNumberField(blank=True, verbose_name='Work phone number')
    workstreet = models.CharField(max_length=50, blank=True, verbose_name='Work street address')
    workcity = models.CharField(max_length=50, verbose_name='Work city', default='Hartford')
    workstate = models.CharField(max_length=50, verbose_name='Work state', default='CT')
    workzip = models.CharField(max_length=5, blank=True, verbose_name='Work zip code')

    capability = models.CharField(max_length=20, choices=CAPABILITY_CHOICES, default='Wintel')
    team = models.CharField(max_length=20, choices=TEAM_CHOICES, default='iBUILD')
    kite = models.BooleanField(default=False, verbose_name='Assigned to KITE project')
    remote = models.BooleanField(default=False, verbose_name='Working remotely')
    csctransfer = models.BooleanField(default=False, verbose_name='Existing CSC employee')
    employid = models.CharField(max_length=15, blank=True, verbose_name='Employee number or PRN')
    employtype = models.CharField(max_length=50, choices=EMPLOY_CHOICES, default='Contractor', verbose_name='Employment Type')

    tokenserial = models.CharField(max_length=15, blank=True, verbose_name='Token serial number')

    class Meta:
        ordering = ['addeddate']
        verbose_name_plural = 'people'
        unique_together = ("firstname", "lastname")

    def __str__(self):
        return '{0} {1}'.format(self.firstname, self.lastname)


class Assignment(models.Model):
    person = models.ForeignKey(Person)
    task = models.ForeignKey(Task)
    comment = models.CharField(max_length=200, blank=True)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.task.title
