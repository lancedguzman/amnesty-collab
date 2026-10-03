from rest_framework import serializers

class LandingPageSerializer(serializers.Serializer):
    hero_title = serializers.CharField(max_length=200)
    hero_subtitle = serializers.CharField()

class CandidateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    platform_details = serializers.CharField()

class FaqSerializer(serializers.Serializer):
    question = serializers.CharField(max_length=255)
    answer = serializers.CharField()

class ApproachSerializer(serializers.Serializer):
    methodology = serializers.CharField()
    description = serializers.CharField()

class TimelineSerializer(serializers.Serializer):
    event_name = serializers.CharField(max_length=150)
    event_date = serializers.DateField()

class ApplicationSerializer(serializers.Serializer):
    applicant_name = serializers.CharField(max_length=100)
    status = serializers.CharField(max_length=50)
