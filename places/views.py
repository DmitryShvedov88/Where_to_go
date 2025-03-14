from django.shortcuts import render, get_object_or_404
from places.models import Place
from django.http import JsonResponse
from django.urls import reverse


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
    place = get_object_or_404(
        Place.objects.prefetch_related('images'),
        id=place_id
        )
    response = {
        "title": place.title,
        "imgs": [place_image.image.url for place_image in place.images.all()],
        "description_short": place.short_description,
        "description_long": place.long_description,
        "coordinates": {
            "lng": place.longitude,
            "lat": place.latitude
        }
    }

    return JsonResponse(
        response,
        json_dumps_params={
            'ensure_ascii': False,
            'indent': 2
            }
            )
