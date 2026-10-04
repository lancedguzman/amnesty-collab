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
        return Response({
            "title": "Our Approach: Revolutionizing Youth Engagement in the Philippines",
            "intro": "Young people want real decision-making power, not tokenistic participation! We're not interested in creating mini-adults. Rather, we support genuine youth-led and youth-owned initiatives that challenge dominant narratives with creative, accessible, and hopeful messages. You'll enjoy working with us if you want to:",
            "points": [
                "Shift from participation to shared power, ensuring children and youth influence decision-making processes.",
                "Build safe and enabling environments with strong safeguarding protocols, particularly for children and youth.",
                "Develop age-appropriate engagement approaches tailored specifically to children and youth.",
                "Counter harmful narratives by promoting children and young people's rights, agency, and participation.",
                "Integrate well-being and resilience into engagement strategies.",
                "Localize approaches to reflect diverse contexts and lived realities."
            ]
        }, status=status.HTTP_200_OK)

class TimelinePageView(APIView):
    def get(self, request):
        return Response({
            "application_timeline": [
                {"date": "Oct 12, 2026", "event": "Applications Open"},
                {"date": "Oct 16, 2026", "event": "Virtual Info Session"},
                {"date": "Nov 9, 2026", "event": "Applications Close"},
                {"date": "Nov 10-13, 2026", "event": "Interview with shortlisted groups"},
                {"date": "Nov 17-20, 2026", "event": "Finalizing of Top 6 groups"},
                {"date": "Nov 24, 2026", "event": "Announcement of Top 6 groups"},
            ],
            "journey_levels": [
                {"level": "Level One", "name": "Online Learning Series", "date_range": "Nov – Dec 2026", "summary": "A series of online learning sessions which aims to provide foundational knowledge and skills necessary for further refining project proposals."},
                {"level": "Level Two", "name": "National Youth Ideathon", "date_range": "Jan 21–26, 2027", "summary": "A 6-day in-person workshop in the Philippines covering creative activism, module design, safeguarding, and final project and budget pitching."},
                {"level": "Level Three", "name": "Mentorship & Project Development", "date_range": "Feb – Apr 2027", "summary": "Monthly virtual coaching to complete mandatory campaign deliverables: MEL framework and Security Plan (Feb), Communications Plan and Branding Kit (Mar), and Operational Plan (Apr)."},
                {"level": "Level Four", "name": "Campaign Rollout", "date_range": "May – Jul 2027", "summary": "Implementation of your 3-month youth-led campaign or HRE initiative."},
                {"level": "Level Five", "name": "Graduation & Retreat", "date_range": "Aug 2027", "summary": "Reflection on collective growth, impact evaluation, project sustainability planning, and celebration."},
            ]
        }, status=status.HTTP_200_OK)

class ApplicationPageView(APIView):
    def get(self, request):
        return Response({"message": "Application Page API endpoint active"}, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = ApplicationSerializer(data=request.data)
        if serializer.is_valid():
            # Save application logic here
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
