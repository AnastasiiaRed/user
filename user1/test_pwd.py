from django.test import TestCase
from django.urls import reverse, resolve
from django.contrib.auth import get_user_model
from user1.views import register
from user1.forms import CreateUserForm


User = get_user_model()

class RegisterViewTests_without_pass(TestCase):

    def setUp(self):
        url = reverse('user1:register')
        self.response = self.client.get(url)

    def test_signup_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_contains_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, CreateUserForm)

    def test_form_inputs(self):
        self.assertContains(self.response, '<input', 5)
        self.assertContains(self.response, 'type="email"', 1)
        self.assertContains(self.response, 'type="password"', 2)


class SuccessfulSignUpTests_without_pwd(TestCase):

    def setUp(self):
        url = reverse('user1:register')
        data = {
		    'username':'123=',
            'email': '123@mail.com'}

        self.response = self.client.post(url, data)
        self.assertContains(self.response, 'password')
