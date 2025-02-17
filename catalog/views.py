from django.shortcuts import render
from catalog.models import Place, Image

# Create your views here.
def index(request):
    print("def index(request)")
    places = Place.objects.all()
    print("places")
    print(places)
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
    print("features")
    print(features)
    context = {
        "places": {
        "type": "FeatureCollection",
        "features": features}
    }
    print("context")
    print(context)

    return render(request, "index.html", context=context)
