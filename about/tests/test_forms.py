from django.test import TestCase
from about.forms import CollaborateForm


class TestCollaborateForm(TestCase):
    """Tests for the CollaborateForm"""

    def test_form_is_valid(self):
        """Form should be valid with correct data"""
        form = CollaborateForm({
            "name": "Matt",
            "email": "test@test.com",
            "message": "Hello!",
        })
        self.assertTrue(form.is_valid())

    def test_name_is_required(self):
        """Name field is required"""
        form = CollaborateForm({
            "name": "",
            "email": "test@test.com",
            "message": "Hello!",
        })
        self.assertFalse(
            form.is_valid(),
            msg="Form valid without name",
        )

    def test_email_is_required(self):
        """Email field is required"""
        form = CollaborateForm({
            "name": "Matt",
            "email": "",
            "message": "Hello!",
        })
        self.assertFalse(
            form.is_valid(),
            msg="Form valid without email",
        )

    def test_message_is_required(self):
        """Message field is required"""
        form = CollaborateForm({
            "name": "Matt",
            "email": "test@test.com",
            "message": "",
        })
        self.assertFalse(
            form.is_valid(),
            msg="Form valid without message",
        )
