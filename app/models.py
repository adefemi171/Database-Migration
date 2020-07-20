from django.db import models

# Create your models here.
class Covid_data(models.Model):
    class Meta:
        db_table = "covid_timeseries"
        
    data_as_of = models.DateTimeField(verbose_name='date_as_of')
    Start_week = models.DateTimeField(verbose_name='Start_week')
    End_Week = models.DateTimeField(verbose_name='End_Week')
    State = models.TextField(verbose_name='State')
    Sex = models.TextField(verbose_name='Sex')
    Age_group = models.TextField(verbose_name='Age_group')
    covid_deaths = models.IntegerField(verbose_name='covid_death')
    total_deaths = models.IntegerField(verbose_name='total_death')
    pneumonia_deaths = models.IntegerField(verbose_name='pneumonia_deaths')
    Pneumonia_andCovid_deaths = models.IntegerField(verbose_name='Pneumonia_andCovid_deaths')
    influenza_deaths = models.IntegerField(verbose_name='influenza_deaths')
    pneumonia_influenzaAndcovid_deaths = models.IntegerField(verbose_name='pneumonia_influenzaAndcovid_deaths')
    foot_note = models.TextField(verbose_name='foot_note',default='')
        