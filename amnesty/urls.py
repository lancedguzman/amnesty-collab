from django.urls import path
from . import views

urlpatterns = [
    path('landing/', views.LandingPageView.as_view(), name='api-landing'),
    path('candidates/', views.CandidatePageView.as_view(), name='api-candidates'),
    path('faqs/', views.FaqsPageView.as_view(), name='api-faqs'),
    path('approach/', views.ApproachPageView.as_view(), name='api-approach'),
    path('timeline/', views.TimelinePageView.as_view(), name='api-timeline'),
    path('application/', views.ApplicationPageView.as_view(), name='api-application'),
]
