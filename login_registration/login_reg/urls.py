from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index),
    path('shows', views.home),
    path('shows/new', views.newShow),
    path('shows/create', views.createShow),
    path('shows/<int:show_id>', views.readShow),
    path('shows/<int:show_id>/edit', views.editShow),
    path('shows/<int:show_id>/update', views.updateShow),
    path('shows/<int:show_id>/delete', views.deleteShow)
]