from django.core.management.base import BaseCommand

from fillari.models import Journey

class Command(BaseCommand):
    help = 'Clears the database of all journey data'

    def handle(self, *args, **kwargs):
       Journey.objects.all().delete()
       self.stdout.write('Journey data deleted successfully')