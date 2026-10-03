from django.urls import path
from . import views

urlpatterns = [
    path('api/landing/', views.LandingPageView.as_view(), name='api-landing'),
    path('api/candidates/', views.CandidatePageView.as_view(), name='api-candidates'),
    path('api/faqs/', views.FaqsPageView.as_view(), name='api-faqs'),
    path('api/approach/', views.ApproachPageView.as_view(), name='api-approach'),
    path('api/timeline/', views.TimelinePageView.as_view(), name='api-timeline'),
    path('api/application/', views.ApplicationPageView.as_view(), name='api-application'),
]
