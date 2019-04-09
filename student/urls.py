from django.urls import path
from .views import CandidateList,CandidateCreate, CandidateDetail, CandidateDelete,CandidateUpdate
app ="stud"
urlpatterns = [
    path('', CandidateList.as_view(), name="student-list"),
    path('student-add/', CandidateCreate.as_view(), name="student-add"),
    path('student/<int:pk>/', CandidateDetail.as_view(), name="student-detail"),
    path('student/<int:pk>/delete', CandidateDelete.as_view(), name="student-delete"),
    path('student/<int:pk>/update', CandidateUpdate.as_view(), name="student-update"),
   
]