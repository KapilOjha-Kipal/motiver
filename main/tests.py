from django.test import TestCase, Client
from .models import Contact

class ContactFormTest(TestCase):
    def test_contact_form_submission(self):
        c = Client()
        response = c.post('/', {
            'name': 'Test User',
            'email': 'test@example.com',
            'subject': 'Test Subject',
            'message': 'Test Message'
        })
        # Check for redirect (302) or success (200) depending on implementation
        # In our view we redirect, so we expect 302
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Contact.objects.filter(email='test@example.com').exists())
