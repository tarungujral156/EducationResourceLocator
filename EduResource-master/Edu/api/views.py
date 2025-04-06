import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

class NearbySearchView(APIView):
    def get(self, request, *args, **kwargs):
        location = request.query_params.get('location')
        radius = request.query_params.get('radius', 1500)
        place_type = request.query_params.get('type', 'library')

        if not location:
            return Response({"error": "Location parameter is required"}, status=status.HTTP_400_BAD_REQUEST)

        api_key = settings.GOOGLE_MAPS_API_KEY
        eventbrite_api_key = settings.EVENTBRITE_API_KEY

        # Fetch places from Google Places API
        google_places_url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={location}&radius={radius}&type={place_type}&key={api_key}"
        places_response = requests.get(google_places_url)
        places_data = places_response.json() if places_response.status_code == 200 else {}

        # Fetch educational events and workshops from Eventbrite API
        eventbrite_url = f"https://www.eventbriteapi.com/v3/events/search/?location.latitude={location.split(',')[0]}&location.longitude={location.split(',')[1]}&location.within={radius}m&categories=101&subcategories=1001,1002&token={eventbrite_api_key}"
        events_response = requests.get(eventbrite_url)
        events_data = events_response.json() if events_response.status_code == 200 else {}

        return Response({
            "places": places_data.get('results', []),
            "events": events_data.get('events', [])
        }, status=status.HTTP_200_OK)


@csrf_exempt
def place_details(request):
    place_id = request.GET.get('placeId')
    api_key = settings.GOOGLE_MAPS_API_KEY
    url = f'https://maps.googleapis.com/maps/api/place/details/json?place_id={place_id}&fields=formatted_phone_number,website&key={api_key}'

    try:
        response = requests.get(url)
        return JsonResponse(response.json())
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

