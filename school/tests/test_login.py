from django.contrib.auth.models import User
from django.test import TestCase,  Client
from django.urls import reverse

class loginTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.login_url = reverse('login')
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123',
            email='test@example.com'
        )

    def test_login_success(self):
        response = self.client.post(self.login_url,{
            'username' : 'testuser',
            'password' : 'testpass123'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('index'))
        self.assertTrue('_auth_user_id' in self.client.session)

    def test_login_fail(self):
        response = self.client.post(self.login_url,{
            'username' : 'testuser',
            'password' : 'passwrong'
        })

        self.assertContains(response, "Usuario y/o contraseña incorrecta")
        self.assertFalse('_auth_user_id' in self.client.session)
