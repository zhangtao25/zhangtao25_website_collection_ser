from django.urls import path

from . import views

urlpatterns = [
    path('add_data', views.add_data, name='add_data'),
    path('get_data', views.get_data, name='get_data')
]