from django.test import TestCase
from .models import FAQ

class FAQTestCase(TestCase):
    def setUp(self):
        self.faq = FAQ.objects.create(question="What is Django?", answer="Django is a web framework.")

    def test_faq_creation(self):
        self.assertEqual(self.faq.question, "What is Django?")

    def test_faq_translation(self):
        self.assertTrue(self.faq.question_hi)  # Check if translation exists

    def test_get_translated_question(self):
        translated_question = self.faq.get_translated_question('hi')
        self.assertEqual(translated_question, self.faq.question_hi)
