from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .models import candidate
# Create your views here.

""" def studentList(request):
    return render(request,"student/list.html") """


class CandidateList(ListView):
    model = candidate
    template_name = 'student/list.html'
    paginate_by = 10

class CandidateDetail(DetailView):
    model = candidate
    template_name = 'student/detail.html'


class CandidateCreate(CreateView):
    model = candidate
    # fields = ('admno','name','fname','dob','gender','phone','std','section','active')
    fields = '__all__'
    template_name = 'student/add.html'


class CandidateUpdate(UpdateView):
    model = candidate
    ''' fields = ('admno','name','fname','dob','gender','phone','std','section','active') '''
    fields = '__all__'
    template_name  ='student/add.html'

class CandidateDelete(DeleteView):
    model = candidate
    success_url = reverse_lazy('student-list')
    # it delete data on confirm as well as on cancel. 