from django.core.management.base import BaseCommand
from epicevents_v2.init_groups import init_groups

class Command(BaseCommand):
    help = 'Initialize groups and their permissions'

    def handle(self, *args, **options):
        init_groups()
        self.stdout.write(self.style.SUCCESS('Groups initialized successfully.'))
