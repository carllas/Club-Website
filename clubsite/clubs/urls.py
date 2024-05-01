from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('clubs/', views.clubs, name='clubs'),
    path('clubs/details/<int:id>', views.details, name='details'),

]