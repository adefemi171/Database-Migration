import datetime
import jwt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from app.models import Covid_data
import pandas as pd

#import_Data
covid_data = pd.read_csv('app/Provisional_COVID-19_Death_Counts_by_Sex__Age__and_State.csv')
covid_data.fillna(0,inplace=True)
covid_data['Data as of'] = pd.to_datetime(covid_data['Data as of'])
covid_data['Start week'] = pd.to_datetime(covid_data['Start week'])
covid_data['End Week'] = pd.to_datetime(covid_data['End Week'])


# Create your views here.
@api_view(["GET"])
def index_page(request):
    #Migrate_data
    i = 0
    while i <= covid_data.shape[0]-1:
        dataAsOf = covid_data['Data as of'][i]
        startWeek = covid_data['Start week'][i]
        endWeek = covid_data['End Week'][i]
        state = covid_data['State'][i]
        sex = covid_data['Sex'][i]
        ageGroup = covid_data['Age group'][i]
        covid_death = covid_data['COVID-19 Deaths'][i]
        totalDeath = covid_data['Total Deaths'][i]
        pneumoniaDeath = covid_data['Pneumonia Deaths'][i]
        pneumoniacovidDeath = covid_data['Pneumonia and COVID-19 Deaths'][i]
        influenzaDeath = covid_data['Influenza Deaths'][i]
        pneumoniaInfluenzaCovid = covid_data['Pneumonia, Influenza, or COVID-19 Deaths'][i]
        footnote = covid_data['Footnote'][i]
        data = Covid_data(
            data_as_of= dataAsOf,
            Start_week= startWeek,
            End_Week = endWeek,
            State = state,
            Sex = sex,
            Age_group = ageGroup,
            covid_deaths = covid_death,
            total_deaths = totalDeath,
            pneumonia_deaths = pneumoniaDeath,
            Pneumonia_andCovid_deaths = pneumoniaInfluenzaCovid,
            influenza_deaths = influenzaDeath,
            pneumonia_influenzaAndcovid_deaths = pneumoniaInfluenzaCovid
            
        )
        data.save()
        print(f"Added row {i} to Database")
        i += 1
    return_data = {
        "error" : "0",
        "message" : "Data Migrated",
        "user_ip" : f"{request.META.get('REMOTE_ADDR', None)} {request.META.get('HTTP_USER_AGENT', '')}"
    }
    return Response(return_data) 
