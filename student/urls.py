from django.urls import path
from .views import CandidateList,CandidateCreate

urlpatterns = [
    path('student/', CandidateList.as_view(), name="student-list"),
    path('student-add/', CandidateCreate.as_view(), name="student-add"),
    
]