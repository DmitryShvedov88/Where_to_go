import os
import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand, CommandError
from requests.exceptions import HTTPError

from places.models import Place, Image


class Command(BaseCommand):
    help = 'Download JSON files in DB'

    def load_image(self, place, place_images):
        """Download photo for particular place"""
        for number, image_url in enumerate(place_images, 1):
            if image_url:
                try:
                    response = requests.get(image_url)
                    image_name = os.path.basename(image_url)
                    response.raise_for_status()
                    if response.status_code == 200:
                        Image.objects.get_or_create(
                            place=place,
                            image=ContentFile(response.content, name=image_name),
                            number=number,
                        )
                        self.stdout.write(
                            self.style.SUCCESS(
                                f"Image: {image_name} has been successfully added to the database"
                            )
                        )
                except HTTPError:
                    self.stderr.write(self.style.ERROR(f"Image loading error code {response.status_code}"))
                except ConnectionError:
                    self.stderr.write(self.style.ERROR(f"Connection error {response.status_code}"))


    def load_place(self, json_url):
        """Download json_place from site"""
        response = requests.get(json_url)
        response.raise_for_status()
        if response.status_code == 200:
            plaсe_payload = response.json()
            plaсe, plaсe_created = Place.objects.get_or_create(
                title=plaсe_payload['title'],
                defaults={
                    'short_description': plaсe_payload['description_short'],
                    'long_description': plaсe_payload['description_long'],
                    'latitude': plaсe_payload['coordinates']['lat'],
                    'longitude': plaсe_payload['coordinates']['lng']
                }
            )
            self.stdout.write(
                self.style.SUCCESS(
                    f"Place: {plaсe} has been successfully added to the database"
                )
            )
            if not plaсe_created:
                raise CommandError('This place already load')
            place_images = (plaсe_payload['imgs'])
            try:
                self.load_image(plaсe, place_images)
            except HTTPError:
                print('json_url "%s" does not exist')
            except ConnectionError:
                print('Connection problem')

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
        parser.add_argument('json_url',
                            type=str,
                            help='Add the url to json file')
