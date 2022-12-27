from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
import csv

def index(request):
    return redirect(reverse('bus_stations'))

with open('data-398-2018-08-30.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    CONTENT = [str(i) for i in reader]

def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    page_num = int(request.GET.get("page", 1))
    paginator = Paginator(CONTENT, 10)
    page = paginator.get_page(page_num)
    context = {
    #     'bus_stations': ...,
    #     'page': ...,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
