from django.test import TestCase, client
from django.conf import settings

from .models import Account


class TestAccountModel(TestCase):
    clietn = client.Client()

    def setUp(self):
        self.account = Account.objects.create_user(username='test1')
        self.super_user = Account.objects.create_superuser(username='testsuper',
                                                           email='testsuper@test.ru',
                                                           password='TestSuper')

    def test_check_password(self):
        self.assertEqual(self.account.username, 'test1')
        self.assertFalse(self.account.password is None)

    def test_superuser(self):
        self.client.login(username='testsuper', password='TestSuper')
        self.response = self.client.get('/admin/')
        self.assertEqual(self.response.context.get('user').username, 'testsuper')
