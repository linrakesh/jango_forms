from django.shortcuts import render
from django.views.generic import ListView, DetailView,CreateView,UpdateView,DeleteView
from .models import candidate
# Create your views here.

class studentList(ListView):
    model = candidate
    template = 'student/list.html'