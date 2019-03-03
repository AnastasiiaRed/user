from django.test import TestCase
from user1 import views
from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TransactionTestCase, Client


class UserHistoryTest(TransactionTestCase):
    user = User.objects.create(username='l', password='pass@123', email='admin@admin.com')
    client = Client() # May be you have missed this line

    def test_history(self):
        self.client.login(username=self.user.username, password='pass@123')
        # get_history function having login_required decorator
        response = self.client.post(reverse(views.index), {'id': self.user.id})
        self.assertEqual(response.status_code, 200) 