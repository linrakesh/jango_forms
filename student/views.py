from django.shortcuts import render
from django.views.generic import ListView, DetailView,CreateView,UpdateView,DeleteView
from .models import candidate
# Create your views here.

""" def studentList(request):
    return render(request,"student/list.html") """


class CandidateList(ListView):
    model = candidate
    template_name = 'student/list.html'
    paginate_by = 3

class CandidateCreate(CreateView):
    model = candidate
    # fields = ('admno','name','fname','dob','gender','phone','std','section','active')
    fields = '__all__'
    template_name = 'student/add.html'
