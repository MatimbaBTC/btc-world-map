from django.core.management.base import BaseCommand
from django.utils import timezone
from events.models import Event

class Command(BaseCommand):
    help = "Delet expired events"

    def handle(self, *args, **options):
        expired = Event.objects.filter(start_data_lt=timezone.now())
        count = expired.count()
        expired.delete()
        self.stdout.write(self.style.SUCCESS(f"{count} expired events deleted"))