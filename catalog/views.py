from django.shortcuts import render, get_object_or_404
from catalog.models import Place, Image
from django.http import JsonResponse, HttpResponse
from django.urls import reverse

# Create your views here.
def index(request):
    places = Place.objects.all()
    features = [
        {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.longitude, place.latitude]
                },
            "properties": {
                "title": place.title,
                "placeId": place.id,
                "detailsUrl": reverse("place_detail", args=[place.id])
                }
        }
        for place in places
        ]
    context = {
        "places": {
            "type": "FeatureCollection",
            "features": features
            }
        }
    return render(request, "index.html", context=context)


def place_detail(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    place_images = place.images.all()
    response = {
        "title": place.title,
        "imgs": [place_image.image.url for place_image in place_images],
        "description_short": place.short_description,
        "description_long": place.long_description,
        "coordinates": {
            "lng": place.longitude,
            "lat": place.latitude
        }
    }

    return JsonResponse(response, json_dumps_params={'ensure_ascii': False, 'indent': 2})
