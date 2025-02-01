from rest_framework import serializers
from django.http import JsonResponse
from .models import FAQ


class FAQSerializer(serializers.ModelSerializer):
    question = serializers.SerializerMethodField()
    answer = serializers.SerializerMethodField()

    class Meta:
        model = FAQ
        fields = ['id', 'question', 'answer']

    def get_question(self, obj):
        lang = self.context.get('lang', 'en')
        return obj.get_translated_question(lang)

    def get_answer(self, obj):
        lang = self.context.get('lang', 'en')
        return obj.get_translated_answer(lang)

def faq_list(request):
    data = [
        {"question": "What is Django?", "answer": "Django is a Python web framework."},
        {"question": "How to install Django?", "answer": "Run pip install django."}
    ]
    return JsonResponse(data, safe=False)