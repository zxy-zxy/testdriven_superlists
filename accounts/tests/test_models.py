from django.test import TestCase
from django.contrib.auth import get_user_model, login

User = get_user_model()
from accounts.models import Token


class UserModelTest(TestCase):
    def test_user_is_valid_with_email_only(self):
        user = User(email='a@b.com')
        user.full_clean()

    def test_email_is_primary_key(self):
        user = User(email='a@b.com')
        self.assertEqual(user.pk, 'a@b.com')

    def test_no_problem_with_auth_login(self):
        user = User.objects.create(email='edith@example.com')
        user.backend = ''
        request = self.client.request().wsgi_request
        login(request, user)


class TokenModelTest(TestCase):
    def test_links_user_with_auto_generated_url(self):
        token1 = Token.objects.create(email='a@b.com')
        token2 = Token.objects.create(email='a@b.com')
        self.assertEqual(token1.uid, token2.uid)
