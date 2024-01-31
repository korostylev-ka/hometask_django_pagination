import csv
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings


def index(request):
    return redirect(reverse('bus_stations'))

def bus_stations(request):
    file = settings.BUS_STATION_CSV
    bus_stations = []
    page_number = int(request.GET.get('page', 1))
    with open(file, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        bus_stations = list(reader)
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    paginator = Paginator(bus_stations, 10)
    page = paginator.get_page(page_number)
    context = {
        'bus_stations': page,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
