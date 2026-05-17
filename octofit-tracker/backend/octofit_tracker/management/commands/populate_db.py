from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

from octofit_tracker import models as octo_models

from django.db import connection

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete all data
        User = get_user_model()
        User.objects.all().delete()
        octo_models.Team.objects.all().delete()
        octo_models.Activity.objects.all().delete()
        octo_models.Leaderboard.objects.all().delete()
        octo_models.Workout.objects.all().delete()

        # Create Teams
        marvel = octo_models.Team.objects.create(name='Marvel')
        dc = octo_models.Team.objects.create(name='DC')

        # Create Users
        ironman = User.objects.create_user(username='ironman', email='ironman@marvel.com', password='pass', team=marvel)
        captain = User.objects.create_user(username='captain', email='captain@marvel.com', password='pass', team=marvel)
        batman = User.objects.create_user(username='batman', email='batman@dc.com', password='pass', team=dc)
        superman = User.objects.create_user(username='superman', email='superman@dc.com', password='pass', team=dc)

        # Create Activities
        octo_models.Activity.objects.create(user=ironman, type='run', duration=30, calories=300)
        octo_models.Activity.objects.create(user=captain, type='cycle', duration=45, calories=400)
        octo_models.Activity.objects.create(user=batman, type='swim', duration=60, calories=500)
        octo_models.Activity.objects.create(user=superman, type='run', duration=50, calories=600)

        # Create Workouts
        octo_models.Workout.objects.create(name='Morning Cardio', description='Cardio for all heroes', duration=40)
        octo_models.Workout.objects.create(name='Strength Training', description='Strength for all heroes', duration=60)

        # Create Leaderboard
        octo_models.Leaderboard.objects.create(user=ironman, score=1000)
        octo_models.Leaderboard.objects.create(user=captain, score=900)
        octo_models.Leaderboard.objects.create(user=batman, score=950)
        octo_models.Leaderboard.objects.create(user=superman, score=1100)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
