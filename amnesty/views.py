from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import (
    LandingPageSerializer, CandidateSerializer, FaqSerializer,
    ApproachSerializer, TimelineSerializer, ApplicationSerializer
)

class LandingPageView(APIView):
    def get(self, request):
        # Placeholder for querying your database
        return Response({"message": "Landing Page API endpoint active"}, status=status.HTTP_200_OK)

class CandidatePageView(APIView):
    def get(self, request):
        return Response({"message": "Candidate Page API endpoint active"}, status=status.HTTP_200_OK)

class FaqsPageView(APIView):
    def get(self, request):
        return Response({"message": "FAQs Page API endpoint active"}, status=status.HTTP_200_OK)

class ApproachPageView(APIView):
    def get(self, request):
        return Response({"message": "Approach Page API endpoint active"}, status=status.HTTP_200_OK)

class TimelinePageView(APIView):
    def get(self, request):
        return Response({"message": "Timeline Page API endpoint active"}, status=status.HTTP_200_OK)

class ApplicationPageView(APIView):
    def get(self, request):
        return Response({"message": "Application Page API endpoint active"}, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = ApplicationSerializer(data=request.data)
        if serializer.is_valid():
            # Save application logic here
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
