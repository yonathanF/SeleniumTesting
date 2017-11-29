from django.test import TestCase
from simpleforms.models import Quote

class QuoteTestCase(TestCase):
    def setUp(self):
        Quote.objects.create(content="TEST TEST", author="Tester 1")
        Quote.objects.create(content="Amazing Quote", author="Tester 2")

    def test_quote_exists(self):
        quote=Quote.objects.get(author="Tester 1")
        self.assertEqual(quote.content, "TEST TEST")
