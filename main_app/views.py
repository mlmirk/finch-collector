from django.shortcuts import redirect, render
from .models import Finch , Snacks
from django.views.generic.edit import CreateView , UpdateView ,DeleteView
from django.views.generic import ListView, DetailView
from main_app import models
from .forms import SightingForm
#Create your views here.




def home(request):
  return render(request,'home.html')

def about(request):
  return render(request, 'about.html')

def finches_index(request):
  finches= Finch.objects.all()
  return render(request, 'finches/index.html', {'finches':finches})

def finches_detail(request,finch_id):
  finch=Finch.objects.get(id=finch_id)
  snacks_finch_doesnt_have = Snacks.objects.exclude(id__in = finch.snacks.all().values_list('id'))
  sighting_form= SightingForm()
  return render(request,'finches/detail.html', {'finch' : finch, 'sighting_form': sighting_form ,'snacks': snacks_finch_doesnt_have,
} )

class FinchCreate(CreateView):
  model= Finch
  fields=['name', 'breed', 'description', 'age']
  
class FinchUpdate(UpdateView):
  model=Finch
  fields = ['species', 'description', 'age']
  

class FinchDelete(DeleteView):
  model=Finch
  fields='__all__'
  success_url='/finches/'

def add_sighting(request, finch_id):
  form= SightingForm(request.POST)
  if form.is_valid():
    new_sighting=form.save(commit=False)
    new_sighting.finch_id= finch_id
    new_sighting.save()
  return redirect("finches_detail", finch_id = finch_id)

class SnacksCreate(CreateView):
  model = Snacks
  fields = '__all__'


class SnacksList(ListView):
  model = Snacks

class SnacksDetail(DetailView):
  model = Snacks

class SnacksUpdate(UpdateView):
  model = Snacks
  fields = ['name', 'color']

class SnacksDelete(DeleteView):
  model = Snacks
  success_url = '/snacks/'

def assoc_snacks(request, finch_id, snacks_id):
  # Note that you can pass a toy's id instead of the whole object
  Finch.objects.get(id=finch_id).snacks.add(snacks_id)
  return redirect('finches_detail', finch_id=finch_id)