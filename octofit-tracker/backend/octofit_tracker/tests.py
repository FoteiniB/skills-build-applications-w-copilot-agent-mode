from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Test Team')
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='pass', team=self.team)
        self.workout = Workout.objects.create(name='Test Workout', description='desc', duration=30)
        self.activity = Activity.objects.create(user=self.user, type='run', duration=20, calories=200)
        self.leaderboard = Leaderboard.objects.create(user=self.user, score=100)

    def test_user_team(self):
        self.assertEqual(self.user.team.name, 'Test Team')
    def test_activity(self):
        self.assertEqual(self.activity.calories, 200)
    def test_workout(self):
        self.assertEqual(self.workout.name, 'Test Workout')
    def test_leaderboard(self):
        self.assertEqual(self.leaderboard.score, 100)
