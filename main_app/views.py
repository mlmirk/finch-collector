from django.shortcuts import redirect, render
from .models import Finch , Snacks
from django.views.generic.edit import CreateView , UpdateView ,DeleteView
from django.views.generic import ListView, DetailView
from main_app import models
from .forms import SightingForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
#Create your views here.




def home(request):
  return render(request,'home.html')

def about(request):
  return render(request, 'about.html')

@login_required
def finches_index(request):
  finches= Finch.objects.filter(user=request.user)
  return render(request, 'finches/index.html', {'finches':finches})

@login_required
def finches_detail(request,finch_id):
  finch=Finch.objects.get(id=finch_id)
  snacks_finch_doesnt_have = Snacks.objects.exclude(id__in = finch.snacks.all().values_list('id'))
  sighting_form= SightingForm()
  return render(request,'finches/detail.html', {'finch' : finch, 'sighting_form': sighting_form ,'snacks': snacks_finch_doesnt_have,
} )


class FinchCreate(LoginRequiredMixin, CreateView):
  model= Finch
  fields=['name', 'breed', 'description', 'age']
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)


class FinchUpdate(LoginRequiredMixin, UpdateView):
  model=Finch
  fields = ['species', 'description', 'age']
  

class FinchDelete(LoginRequiredMixin, DeleteView):
  model=Finch
  fields='__all__'
  success_url='/finches/'

@login_required
def add_sighting(request, finch_id):
  form= SightingForm(request.POST)
  if form.is_valid():
    new_sighting=form.save(commit=False)
    new_sighting.finch_id= finch_id
    new_sighting.save()
  return redirect("finches_detail", finch_id = finch_id)

class SnacksCreate(LoginRequiredMixin, CreateView):
  model = Snacks
  fields = '__all__'


class SnacksList(LoginRequiredMixin, ListView):
  model = Snacks

class SnacksDetail(LoginRequiredMixin, DetailView):
  model = Snacks

class SnacksUpdate(LoginRequiredMixin, UpdateView):
  model = Snacks
  fields = ['name', 'color']

class SnacksDelete(LoginRequiredMixin, DeleteView):
  model = Snacks
  success_url = '/snacks/'

@login_required
def assoc_snacks(request, finch_id, snacks_id):
  # Note that you can pass a toy's id instead of the whole object
  Finch.objects.get(id=finch_id).snacks.add(snacks_id)
  return redirect('finches_detail', finch_id=finch_id)

class Home(LoginView):
  template_name = 'home.html'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in
      login(request, user)
      return redirect('cats_index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)