from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator

class FAQ(models.Model):
    question_en = models.TextField()
    answer_en = RichTextField()
    question_hi = models.TextField(blank=True, null=True)
    answer_hi = RichTextField(blank=True, null=True)
    question_bn = models.TextField(blank=True, null=True)
    answer_bn = RichTextField(blank=True, null=True)

    def get_translated_question(self, lang):
        return getattr(self, f'question_{lang}', self.question_en)

    def get_translated_answer(self, lang):
        return getattr(self, f'answer_{lang}', self.answer_en)

    def save(self, *args, **kwargs):
        translator = Translator()
        for lang_code in ['hi', 'bn']:
            question_field = f'question_{lang_code}'
            answer_field = f'answer_{lang_code}'

            # Check if translation is needed
            if not getattr(self, question_field):
                try:
                    setattr(self, question_field, translator.translate(self.question_en, dest=lang_code).text)
                except Exception as e:
                    setattr(self, question_field, self.question_en)

            if not getattr(self, answer_field):
                try:
                    setattr(self, answer_field, translator.translate(self.answer_en, dest=lang_code).text)
                except Exception as e:
                    setattr(self, answer_field, self.answer_en)

        super().save(*args, **kwargs)