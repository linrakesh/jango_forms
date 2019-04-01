from django.urls import path
from .views import studentList

urlpatterns = [
    path('student_list', studentList.as_view(),name="student-list"),
    
]