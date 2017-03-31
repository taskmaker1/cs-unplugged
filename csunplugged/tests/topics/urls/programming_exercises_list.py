from tests.BaseTest import BaseTest
from django.urls import reverse


class ProgrammingExercisesListURLTest(BaseTest):

    def __init__(self, *args, **kwargs):
        BaseTest.__init__(self, *args, **kwargs)

    def test_valid_programming_exercises_list(self):
        url = reverse('topics:programming_exercises_list', args=['binary-numbers', 'unit-plan', 'lesson-1'])
        self.assertEqual(url, '/en/topics/binary-numbers/unit-plan/lesson/lesson-1/plugged-in/')
