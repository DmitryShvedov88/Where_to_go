from django.shortcuts import render
from catalog.models import Place, Image

# Create your views here.
# Create your views here.
def index(request):
    print("Hi")
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
                "placeId": place.id",
                "detailsUrl": "static/places/moscow_legends.json"
                }
        }
        for place in places
        ]

    context = {
        "type": "FeatureCollection",
        "features": features}

    return render(request, "index.html", context=context)
