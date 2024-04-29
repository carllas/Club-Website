from django.core.management.base import BaseCommand
from clubs.models import Club  # Replace "myapp" with your actual app name

class Command(BaseCommand):
    help = 'Insert clubs into the database'

    def handle(self, *args, **options):
        club1 = Club(name='Club A', description='A great club')
        club1.save()
