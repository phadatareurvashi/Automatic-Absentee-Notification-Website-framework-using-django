# your_app/management/commands/arrange_roll_numbers.py

from django.core.management.base import BaseCommand
from notification.models import Student

class Command(BaseCommand):
    help = 'Arrange roll numbers serially'

    def handle(self, *args, **options):
        Student.arrange_roll_numbers()
        self.stdout.write(self.style.SUCCESS('Successfully arranged roll numbers'))
