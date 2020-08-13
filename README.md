# Database Migration

Clone the repository using


## Project Startup
Edit settings.py in [add_data/settings.py](https://github.com/adefemi171/Database-Migration/blob/master/add_data/settings.py) to include your database configuration

Also, note that the csv file am using is from [Centers for Disease Control and Prevention](https://data.cdc.gov/NCHS/Provisional-COVID-19-Death-Counts-by-Sex-Age-and-S/9bhg-hcku) and dated 12th August, 2020

After making the changes run:
```
python manage.py makemigrations
```

Then run 
```
python manage.py migrate
```

Finally run the development server using
```
python manage.py runserver
```

Head over to your browser and you can either send a request or enter in the url 
[http://127.0.0.1:8000/](http://127.0.0.1:8000/)

