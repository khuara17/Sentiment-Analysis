from django.db import models
import datetime

class trendingtopicsmodel(models.Model):
    id = models.AutoField(primary_key=True)
    tagname = models.CharField(max_length=100)
    cdate = models.DateField(default=datetime.date.today)
    tagcount = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.tagname
    class Meta:
        db_table = "trendingtopics"