from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.http import require_POST
import json


VEHICLES = [
    {'name': 'Swift Dzire', 'price': 11, 'capacity': 4, 'type': 'Sedan', 'image': 'home/images/vehicles/swift_dzire.jpg'},
    {'name': 'Ertiga', 'price': 13, 'capacity': 7, 'type': 'MUV', 'image': 'home/images/vehicles/ertiga.jpg'},
    {'name': 'Tavera', 'price': 15, 'capacity': 8, 'type': 'SUV', 'image': 'home/images/vehicles/tavera.jpg'},
    {'name': 'Innova Crysta', 'price': 18, 'capacity': 8, 'type': 'SUV Premium', 'image': 'home/images/vehicles/innova.jpg'},
    {'name': 'Tempo Traveller 14', 'price': 22, 'capacity': 14, 'type': 'Traveller', 'image': 'home/images/vehicles/tempo_14.jpg'},
    {'name': 'Tempo Traveller 17', 'price': 24, 'capacity': 17, 'type': 'Traveller', 'image': 'home/images/vehicles/tempo_17.jpg'},
    {'name': 'Tempo Traveller 20', 'price': 26, 'capacity': 20, 'type': 'Traveller', 'image': 'home/images/vehicles/tempo_20.jpg'},
    {'name': 'Tempo Traveller 26', 'price': 32, 'capacity': 26, 'type': 'Traveller', 'image': 'home/images/vehicles/tempo_26.jpg'},
    {'name': 'Bus 52 Seater', 'price': 70, 'capacity': 52, 'type': 'Bus', 'image': 'home/images/vehicles/bus_52.jpg'},
]

SERVICES = [
    {
        'title': 'Airport Transfer',
        'desc': 'Indore Airport se Ujjain tak seamless pick & drop service',
        'icon': '✈️'
    },
    {
        'title': 'Railway Station',
        'desc': 'Ujjain Railway Station se cab booking available hai',
        'icon': '🚂'
    },
    {
        'title': 'Ujjain Darshan',
        'desc': 'Mahakaleshwar aur sabhi dharmik sthalon ki darshan yatra',
        'icon': '🛕'
    },
    {
        'title': 'Outstation Trips',
        'desc': 'Omkareshwar, Bhopal, Pachmarhi, Indore aur pure India mein',
        'icon': '🗺️'
    },
]


def home(request):
    context = {
        'vehicles': VEHICLES,
        'services': SERVICES,
        'phone': '7241126576',
        'phone2': '7974124869',
        'whatsapp': 'https://api.whatsapp.com/send?phone=7241126576',
        'whatsapp2': 'https://api.whatsapp.com/send?phone=7974124869'
    }
    return render(request, 'home/index.html', context)


@require_POST
def contact_submit(request):
    try:
        data = json.loads(request.body)
        name = data.get('name', '').strip()
        phone = data.get('phone', '').strip()
        message = data.get('message', '').strip()
        if name and phone:
            return JsonResponse({'success': True, 'message': 'Aapka message mil gaya! Hum jald hi sampark karenge.'})
        return JsonResponse({'success': False, 'message': 'Naam aur phone number zaroori hai.'})
    except Exception:
        return JsonResponse({'success': False, 'message': 'Kuch error aa gaya, phir try karein.'})
