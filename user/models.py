from django.db import models
import datetime

class userregistermodel(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.email

    class Meta:
        db_table = "registrations"

class useralgorithammodels(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    appliedalgo = models.CharField(max_length=100)
    datasetname = models.CharField(max_length=100)
    currectrecord = models.PositiveSmallIntegerField()
    totalrecord = models.PositiveSmallIntegerField()
    accuracy = models.FloatField()
    cdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
    class Meta:
        db_table = 'usersearchanalysis'