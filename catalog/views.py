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
    print("context")
    print(context)

    return render(request, "index.html", context=context)


def place_detail(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    place_images = place.images.all()
    response = {
        "title": place.title,
        "imgs": [place_image.image.url for place_image in place_images],
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lng": place.lng,
            "lat": place.lat
        }
    }

    return JsonResponse(response, json_dumps_params={'ensure_ascii': False})
