from django.urls import path
from . import views

urlpatterns = [
    path('', views.condition_view, name='condition_view'),
]
