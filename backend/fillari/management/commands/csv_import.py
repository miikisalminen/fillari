import csv
import os

from django.utils import timezone
from django.core.management.base import BaseCommand

from fillari.models import Journey

# This command imports journey data from the csv files

class Command(BaseCommand):
    help = 'Imports the csv-files to the database'

    def handle(self, *args, **kwargs):
        data_directory = './fillari/management/commands/data'
        start_time = timezone.now()
        for csv_file_name in os.listdir(data_directory):
            file_path = os.path.join(data_directory, csv_file_name)
            with open(file_path, 'r') as csv_file:
                next(csv_file)
                data = csv.reader(csv_file, delimiter=",")
                journeys = []
                for row in data:
                    try:
                        journey = Journey(
                            departure_station = row[3].encode("latin-1").decode(),
                            return_station = row[5].encode("latin-1").decode(),
                            distance = float(row[6]),
                            duration = float(row[7])
                        )
                    except:
                        continue
                    journeys.append(journey)
                    if len(journeys) > 5000:
                        Journey.objects.bulk_create(journeys)
                        journeys = []

        if journeys:
            Journey.objects.bulk_create(journeys)
        
        end_time = timezone.now()
        self.stdout.write(
            self.style.SUCCESS(
                f"Loading CSV took: {(end_time-start_time).total_seconds()} seconds."
            )
        )

