from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path("about/", views.about, name='about'),
    path("finches/", views.finches_index , name="finches_index"),
    path("finches/<int:finch_id>", views.finches_detail, name="finches_detail"),
    path("finches/create/", views.FinchCreate.as_view(), name='finches_create'),
    path('finches/<int:pk>/update',views.FinchUpdate.as_view(), name='finches_update'),
    path('finches/<int:pk>/delete',views.FinchDelete.as_view(), name="finches_delete"),
    path("finches/<int:finch_id>/add_sighting", views.add_sighting, name="add_sighting"),
    path('finches/<int:finch_id>/assoc_snacks/<int:snacks_id>/', views.assoc_snacks, name='assoc_snacks'),
    path('snacks/create/', views.SnacksCreate.as_view(), name='snacks_create'),
    path('snacks/<int:pk>/', views.SnacksDetail.as_view(), name='snacks_detail'),
    path('snacks/', views.SnacksList.as_view(), name='snacks_index'),

    path('snacks/<int:pk>/update/', views.SnacksUpdate.as_view(), name="snacks_update"),
    path('snacks/<int:pk>/delete/', views.SnacksDelete.as_view(), name='snacks_delete'),
    path('accounts/signup/', views.signup, name='signup'),
]
