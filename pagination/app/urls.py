from django.urls import path

from app.views import index, bus_stations, bus_stations_empty


urlpatterns = [
    path('', index, name='index'),
    path('bus_stations/<int:current_page>/', bus_stations, name='bus-stations'),
    path('bus_stations/', bus_stations_empty, name='bus-stations-empty'),

]
