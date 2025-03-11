import requests
import os
from django.core.management.base import BaseCommand, CommandError
from requests.exceptions import HTTPError
from catalog.models import Place, Image
from django.core.files.base import ContentFile


class Command(BaseCommand):
    help = 'Download JSON files in DB'

    def load_image(self, place, place_images):
        """Download photo for particular place"""
        for number, image_url in enumerate(place_images, 1):
            if image_url:
                response = requests.get(image_url)
                image_name = os.path.basename(image_url)
                response.raise_for_status()
                if response.status_code == 200:
                    Image.objects.get_or_create(
                        place=place,
                        image=ContentFile(response.content, name=image_name),
                        number=number,
                    )

    def load_place(self, json_url):
        """Download json_place from site"""
        response = requests.get(json_url)
        response.raise_for_status()
        if response.status_code == 200:
            plaсe_data = response.json()
            plaсe, plaсe_description = Place.objects.get_or_create(
                title=plaсe_data['title'],
                defaults={
                    'short_description': plaсe_data['description_short'],
                    'long_description': plaсe_data['description_long'],
                    'latitude': plaсe_data['coordinates']['lat'],
                    'longitude': plaсe_data['coordinates']['lng']
                    }
                )
            if not plaсe_description:
                raise CommandError('This place already load')
            place_images = (plaсe_data['imgs'])
            self.load_image(plaсe, place_images)

    def handle(self, *args, **options):
        try:
            json_url = options['json_url']
            if json_url:
                self.load_place(json_url)
        except HTTPError:
            print('json_url "%s" does not exist')
        except ConnectionError:
            print('Connection problem')

    def add_arguments(self, parser):
        parser.add_argument('--json_url',
                            type=str,
                            help='Add the url to json file')
