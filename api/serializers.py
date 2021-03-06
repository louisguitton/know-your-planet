from rest_framework import serializers

from api.models import Question, QuestionStat, Contribution


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = [
            'id', 'text', 'type', 'category', 'difficulty', 'author',
            'answer_option_a', 'answer_option_b', 'answer_option_c', 'answer_option_d',
            'answer_correct', 'answer_explanation', 'answer_additional_link', 'answer_image_link',
            'answer_count', 'answer_success_count',
            'created', 'updated'
        ]


class QuestionStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionStat
        fields = [
            'question_id', 'answer_choice', 'created'
        ]

class ContributionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contribution
        fields = [
            'text', 'description', 'created'
        ]