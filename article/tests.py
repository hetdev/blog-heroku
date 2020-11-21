from django.contrib.auth.models import User
from django.test import TestCase

from article.models import Article, ContactRequest


class ArticleTestCase(TestCase):
    def setUp(self):
        user, created = User.objects.get_or_create(
            first_name='Hetzel',
            email='hetzel30@gmail.com',
            username='hetzel30@gmail.com',
        )
        Article.objects.create(author=user,
                               title='Test1 run command',
                               content='Lorem ipsum',
                               active=True,
                               publication_date='2202-01-01 10:20')
        Article.objects.create(author=user,
                               title='Test2 run command',
                               content='Lorem ipsum',
                               publication_date='2202-01-01 10:20')

    def test_articles_created(self):
        article_1 = Article.objects.get(title='Test1 run command')
        article_2 = Article.objects.get(title='Test2 run command')
        self.assertEqual(article_1.slug, 'test1-run-command')
        self.assertEqual(article_2.slug, 'test2-run-command')

        self.assertEqual(article_1.content, 'Lorem ipsum')
        self.assertEqual(article_2.content, 'Lorem ipsum')

        self.assertTrue(article_1.active)
        self.assertFalse(article_2.active)


class ContactRequestTestCase(TestCase):
    def setUp(self):
        ContactRequest.objects.create(name='Test1',
                                      email='test1@email.com',
                                      content='Lorem ipsum',
                                      contact_date='2202-01-01 10:20')
        ContactRequest.objects.create(name='Test2',
                                      email='test2@email.com',
                                      content='Lorem ipsum',
                                      contact_date='2202-01-01 10:20')

    def test_contact_request_created(self):
        contact_request_1 = ContactRequest.objects.get(name='Test1')
        contact_request_2 = ContactRequest.objects.get(name='Test2')

        self.assertEqual(contact_request_1.email, 'test1@email.com')
        self.assertEqual(contact_request_1.content, 'Lorem ipsum')

        self.assertEqual(contact_request_2.email, 'test2@email.com')
        self.assertEqual(contact_request_2.content, 'Lorem ipsum')
