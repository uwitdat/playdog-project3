from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dogs/',views.dogs_index, name="dogs_index"),
    path('dogs/<int:dog_id>/', views.dogs_detail, name='detail'),
    path('dogs/create/', views.DogCreate.as_view(), name='dogs_create'),
    path('dogs/<int:pk>/update/', views.DogUpdate.as_view(), name='dogs_update'),
    path('dogs/<int:pk>/delete/', views.DeleteDog, name='dogs_delete'),
    path('events/',views.events_index, name="events_index"),
    path('events/<int:event_id>/', views.events_detail, name='events_detail'),
    path('events/create/', views.EventCreate.as_view(), name='events_create'),
    path('events/<int:pk>/update/', views.EventUpdate.as_view(), name='events_update'),
    path('events/<int:pk>/delete/', views.DeleteEvent, name='events_delete'),
   
]
