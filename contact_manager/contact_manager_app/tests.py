from django.test import TestCase
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Contact
from rest_framework.authtoken.models import Token

# Unit tests for user registration


class UserCreateViewTest(TestCase):
    def test_user_registration(self):
        data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'testpassword',
        }
        response = self.client.post('/users/create/', data, format='json')
        # Check for successful user registration
        self.assertEqual(response.status_code, 201)
        print("User registration test: Passed")

        # Check if the user was actually created in the database
        user = User.objects.get(username='testuser')
        self.assertEqual(user.email, 'testuser@example.com')
        print("User creation in the database: Passed")

# Unit tests for the contact API endpoints


class ContactAPITests(APITestCase):
    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create_user(
            username="testuser", password="testpassword", email="test@example.com")

    def test_create_contact(self):
        url = reverse('contact_manager_app:contact-create')
        data = {
            'user': self.user.id,
            'first_name': 'John',
            'last_name': 'Doe',
            'phone_number': '1234567890',
        }

        self.client.force_authenticate(user=self.user)  # Authenticate the user
        response = self.client.post(url, data, format='json')

        # Check for successful creation of a contact
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        print("Contact creation test: Passed")

        self.assertEqual(Contact.objects.count(), 1)
        self.assertEqual(Contact.objects.first().first_name, 'John')
        print("Contact created in the database: Passed")

    def test_update_contact(self):
        # Create a contact
        contact = Contact.objects.create(
            user=self.user,
            first_name='Jane',
            last_name='Doe',
            phone_number='9876543210'
        )

        url = reverse('contact_manager_app:contact-update', args=[contact.id])
        data = {
            'user': self.user.id,
            'first_name': 'Updated',
            'last_name': 'Name',
            'phone_number': '5555555555',
        }

        self.client.force_authenticate(user=self.user)  # Authenticate the user
        response = self.client.put(url, data, format='json')

        # Check for successful update of the contact
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        contact.refresh_from_db()
        self.assertEqual(contact.first_name, 'Updated')
        print("Contact update test: Passed")

    def test_update_contact_unauthenticated(self):
        # Create a contact
        contact = Contact.objects.create(
            user=self.user,
            first_name='Jane',
            last_name='Doe',
            phone_number='9876543210'
        )

        url = reverse('contact_manager_app:contact-update', args=[contact.id])
        data = {
            'user': self.user.id,
            'first_name': 'Updated',
            'last_name': 'Name',
            'phone_number': '5555555555',
        }

        # Do not authenticate the user (simulating an unauthenticated user)
        response = self.client.put(url, data, format='json')

        # Check that unauthenticated users receive a 401 Unauthorized status
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        print("Unauthenticated user update test: Passed")


class UserLoginViewTest(APITestCase):
    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create_user(
            username="testuser", password="testpassword", email="test@example.com")

    def test_user_login(self):
        url = reverse('contact_manager_app:user-login')
        data = {
            'username': 'testuser',
            'password': 'testpassword',
        }

        # Create a token for the user
        self.token, _ = Token.objects.get_or_create(user=self.user)

        response = self.client.post(url, data, format='json')

        # Check for successful login
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)
        print("User login test: Passed")

    def test_user_login_invalid_credentials(self):
        url = reverse('contact_manager_app:user-login')
        data = {
            'username': 'testuser',
            'password': 'wrongpassword',  # Incorrect password
        }

        response = self.client.post(url, data, format='json')

        # Check for unsuccessful login with invalid credentials
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        print("Invalid user login test: Passed")


class UserLogoutViewTest(APITestCase):
    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create_user(
            username="testuser", password="testpassword", email="test@example.com")

        # Create a token for the user
        self.token, _ = Token.objects.get_or_create(user=self.user)

    def test_user_logout(self):
        url = reverse('contact_manager_app:user-logout')

        # Authenticate the user by setting the token in the client's credentials
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')

        response = self.client.post(url, format='json')

        # Check for successful logout (token deletion)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print("User logout test: Passed")
