from django.core.management.base import BaseCommand
from ...print_hello import Print_hello

class Command(BaseCommand):
    help = 'Juste say hello'

    def handle(self, *args, **options):
        coucou = Print_hello()
        coucou.print_hello()

