from django.shortcuts import render
from django.http  import HttpResponse
import datetime as dt

def welcome(request):
    return HttpResponse('Welcome to the Hub')


def photo_of_day(request):
    date = dt.date.today()
    html = f'''
       <html>
         <body>
            <h1> {date.day}-{date.month}-{date.year}</h1>

        </body>
        </html>
        '''
    return HttpResponse(html)


def convert_dates(dates):
     # Function that gets the weekday number for the date.
    
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

    # Returning the actual day of the week

    day = days[day_number]
    return day


def photo_of_day(request):
    date = dt.date.today()

    # Function to convert date object to find exact day

    html = f'''
        <html>
          <body>
            <h1>Photo for {day}