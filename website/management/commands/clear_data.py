__author__ = 'faculty'

from website.models import Courses, PreRequisite


from django.core.management.base import BaseCommand, CommandError



class Command(BaseCommand):
    help = "adds sample entities to the application"

    def handle(self, *args, **options):
        Courses.objects.all().delete()
        PreRequisite.objects.all().delete()

