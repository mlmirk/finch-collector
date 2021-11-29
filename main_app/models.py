from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.
Seen= (
  ('M', 'Morning'),
  ('A', 'Afternoon'),
  ('N', 'Night')
)

class Snacks(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('snacks_detail', kwargs={'pk': self.id})

class Finch(models.Model):
  name= models.CharField(max_length=100)
  species= models.CharField(max_length=100)
  description= models.TextField(max_length=250)
  age =models.IntegerField()
  snacks = models.ManyToManyField(Snacks)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('finches_detail', kwargs={'finch_id': self.id})

class Sighting(models.Model):
  date = models.DateField("Sighting Date")
  spotted = models.CharField(
  max_length=1,
  choices=Seen,
  default=Seen[0][0]
  )

  finch = models.ForeignKey(Finch, on_delete=models.CASCADE)



  def __str__(self):
    return f"Seen in the {self.get_spotted_display()} on {self.date}"
  
  class Meta:
    ordering = ['-date']