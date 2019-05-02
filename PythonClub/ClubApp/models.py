from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Meeting(models.Model):
    meetingtitle=models.CharField(max_length=255)
    meetingdate=models.DateField()
    meetingtime=models.TimeField()
    meetinglocation=models.CharField(max_length=255)
    meetingagenda=models.TextField()

    def __str__(self):
        return self.meetingtitle

    class Meta:
        db_table='meeting'
        verbose_name_plural='meetings'

class MeetingMinutes(models.Model):
    meetingminutes=models.CharField(max_length=255)
    meetingID=models.ForeignKey(Meeting,on_delete=models.DO_NOTHING)
    attendance=models.ManyToManyField(User)
    minutes=models.TextField()

    def __str__(self):
        return self.meetingminutes

    class Meta:
        db_table='meetingminutes'
        verbose_name_plural='meetingminutes'

class Resource(models.Model):
    resourcename=models.CharField(max_length=255)
    resourcetype=models.CharField(max_length=255)
    resourceURL=models.URLField()
    user=models.ForeignKey(User,on_delete=models.DO_NOTHING)
    rating=models.SmallIntegerField()
    reviewtext=models.TextField()

    def __str__(self):
        return self.resourcename

    class Meta:
        db_table='resource'
        verbose_name_plural='resources'

class Events(models.Model):
    eventname=models.CharField(max_length=255)
    eventlocation=models.CharField(max_length=255)
    eventdatetime=models.DateTimeField()
    eventdescription=models.TextField()
    user=models.ForeignKey(User,on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.eventname

    class Meta:
        db_table='events'
        verbose_name_plural='events'


