from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView
from classbased.models import Student


# Create your views here.
class Read_Data(ListView):
    model=Student

class Read_One_Data(DetailView):
    model=Student

class Insert_Data(CreateView):
    model=Student
    fields="__all__"

class Update_Data(UpdateView):
    model=Student
    fields="__all__"
