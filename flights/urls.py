from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='flights-home'),  # or any view you defined
]

