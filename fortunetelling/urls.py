from django.urls import path
from . import views

app_name = 'fortunetelling'
urlpatterns = [
    path('', views.FortuneTelling.as_view(), name='fortunetelling'),
]

