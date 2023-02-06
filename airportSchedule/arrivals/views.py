from django.shortcuts import render
from datetime import date, timedelta
import requests
import os
import json



AEROAPI_KEY = str(os.getenv('AEROAPI_KEY'))
AEROAPI = requests.Session()
AEROAPI.headers.update({"x-apikey": AEROAPI_KEY})

def arrivals(request):

    if request.method == "POST":
        airport = request.POST['airport']
        today = date.today()
        yesterday = today - timedelta(1)
        tomorrow = today + timedelta(1)
        results = AEROAPI.get(f"https://aeroapi.flightaware.com/aeroapi/airports/{airport}/flights/arrivals?start={today}&end={tomorrow}&max_pages=10")

        schedule = results.json()

        arrivals = schedule['arrivals']
        
        context = {
            'arrivals': arrivals,
            'airport': airport,
        }

        print(arrivals)
    else: 
        context = {}
    return render(request, 'arrivals.html', context )
