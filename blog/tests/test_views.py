from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from blog.models import Post, Comment, Category


class TestCommentViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.owner = User.objects.create_user(
            username='owner', password='testpass123')
        self.other = User.objects.create_user(
            username='other', password='testpass123')

        self.category = Category.objects.create(name='Test')

        self.post = Post.objects.create(
            title='Test Post',
            slug='test-post',
            author=self.owner,
            category=self.category,
            content='Test content',
            status=1
        )

        self.comment = Comment.objects.create(
            post=self.post,
            author=self.owner,
            body='Test comment',
            approved=True
        )

    def test_unauthenticated_cannot_edit_comment(self):
        url = reverse('comment_edit', args=[
            self.post.slug, self.comment.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertIn('/accounts/login', response['Location'])

    def test_unauthenticated_cannot_delete_comment(self):
        url = reverse('comment_delete', args=[
            self.post.slug, self.comment.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertIn('/accounts/login', response['Location'])

    def test_non_owner_cannot_edit_comment(self):
        self.client.login(username='other', password='testpass123')
        url = reverse('comment_edit', args=[
            self.post.slug, self.comment.id])
        response = self.client.post(url, {'body': 'hacked'})
        self.assertEqual(response.status_code, 302)

    def test_non_owner_cannot_delete_comment(self):
        self.client.login(username='other', password='testpass123')
        url = reverse('comment_delete', args=[
            self.post.slug, self.comment.id])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(
            Comment.objects.filter(id=self.comment.id).exists()
        )

    def test_owner_can_edit_comment(self):
        self.client.login(username='owner', password='testpass123')
        url = reverse('comment_edit', args=[
            self.post.slug, self.comment.id])
        response = self.client.post(url, {'body': 'updated'})
        self.assertEqual(response.status_code, 302)