from django.core.management.base import BaseCommand
from clubs.models import Club
import os 
import csv

class Command(BaseCommand):
    help = 'Insert clubs into the database'

    def handle(self, *args, **options):
        Club.objects.all().delete()
        print(os.getcwd())
        file = open('clubs/management/commands/clubs.csv')
        reader = csv.reader(file)
        headers = next(reader)
        for row in reader:
            name = row[2]
            description = row[3]
            sponsor_name = row[4]
            sponsor_email = row[5]
            meeting_times = row[7]
            location = row[8]
            club = Club(name=name, description=description, sponsor_name=sponsor_name, sponsor_email=sponsor_email, meeting_times=meeting_times, location=location)
            club.save()
