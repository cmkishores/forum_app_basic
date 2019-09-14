from django.test import TestCase
from .models import Update

class UpdateTest (TestCase):
	def setUp(self):
		'''This function sets up a dummy database
		for the following test function to verify '''
		Update.objects.create(title='Test',comment='TestComment')

	def test_update_contents(self):

		update_object = Update.objects.get(id=1)
		expected_object_title = f'{update_object.title}'
		expected_object_comment = f'{update_object.comment}'
		self.assertEqual(expected_object_comment,'TestComment')
		return self.assertEqual(expected_object_title,'Test')