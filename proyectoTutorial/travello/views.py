from django.shortcuts import render
from .models import Destination

# Create your views here.

def index(request):
    dest1 = Destination()
    dest1.name = 'Peru'
    dest1.desc = 'Un lugar frio en estos dias'
    dest1.price = 250
    dest1.img = 'destination_1.jpg'

    dest2 = Destination()
    dest2.name = 'Argentina'
    dest2.desc = 'Hogar del mas grande'
    dest2.price = 300
    dest2.img = 'destination_2.jpg'

    dest3 = Destination()
    dest3.name = 'Colombia'
    dest3.desc = 'Hogar del Cafe'
    dest3.price = 200
    dest3.img = 'destination_3.jpg'

    dests = [dest1,dest2, dest3]
    return render(request, 'index.html', {'dests': dests})