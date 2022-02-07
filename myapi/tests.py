from django.test import TestCase
from .models import Installation, Status, StatusIndication
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse


class InstallationTestCase(TestCase):
    """This class defines the test suite for the Installation model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.installation = Installation(customer_name = 'Eljoenai Muninga',
            address='15 Fred Street, Fourways, Johannesburg',
            appointment_date = '2022-02-18')
    
    def test_model_can_create_a_installation(self):
        """Test the Installation model can create an installation."""
        old_count = Installation.objects.count()
        self.installation.save();
        new_count = Installation.objects.count()
        self.assertNotEqual(old_count, new_count)


class StatusTestCase(TestCase):
    """This class defines the test suite for the Status model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.installation = Installation(customer_name = 'Eljoenai Muninga',
            address='15 Fred Street, Fourways, Johannesburg',
            appointment_date = '2022-02-18')
        self.installation.save();
        self.status = Status(status = StatusIndication.IN_PROGRESS,
            notes='This is a very nice note to see',
            installation = self.installation)
    
    def test_model_can_create_a_status(self):
        """Test the Installation model can create an status."""
        old_count = Status.objects.count()
        self.status.save();
        new_count = Status.objects.count()
        self.assertNotEqual(old_count, new_count)


class ViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.installation_data = {'customer_name': 'John Muninga', 'address' : '32 Mayo Street, Blackheath, Randburg', 'appointment_date': '2022-02-19'}
        self.response = self.client.post(
            '/create/installation/',
            self.installation_data,
            format="json")

    def test_api_can_create_a_installation(self):
        """Test the api has installation creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)