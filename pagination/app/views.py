from django.shortcuts import render_to_response, redirect
from django.urls import reverse
import csv
from django.conf import settings
from django.core.paginator import Paginator

with open(settings.BUS_STATION_CSV, encoding='cp1251') as file:
    data = list(csv.DictReader(file))

def index(request):
    return redirect(reverse(bus_stations , args=[1,]))

def bus_stations_empty(request):
    return redirect(reverse(bus_stations, args=[1,]))

def bus_stations(request, current_page):
    paginator = Paginator(data, 10)
    if current_page not in paginator.page_range:
        current_page = 1
    page = paginator.page(current_page)
    next_page_url = reverse(bus_stations, args=[page.next_page_number(),]) if page.has_next() else None
    prev_page_url = reverse(bus_stations, args=[page.previous_page_number(),]) if page.has_previous() else None
    return render_to_response('index.html', context={
        'bus_stations': page.object_list,
        'current_page': page.number,
        'prev_page_url': prev_page_url,
        'next_page_url': next_page_url,
    })

