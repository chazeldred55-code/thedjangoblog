from django.test import TestCase

from ..forms import CommentForm


class TestCommentForm(TestCase):

    def test_form_is_valid(self):
        form = CommentForm(
            {
                "body": "This is a test comment",
            }
        )
        self.assertTrue(form.is_valid())

    def test_form_is_invalid(self):
        form = CommentForm(
            {
                "body": "",
            }
        )
        self.assertFalse(form.is_valid())
        self.assertIn("body", form.errors)
