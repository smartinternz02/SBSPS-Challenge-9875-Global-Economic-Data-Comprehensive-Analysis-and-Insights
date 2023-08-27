
from django.urls import path
from . import views

urlpatterns = [
    path('', views.BASE, name='BASE'),
    path('base.html', views.BASE),
    path('report.html', views.REPORT),
    path('story.html', views.STORY),
    path('vision.html', views.VISION),
    path('team.html', views.TEAM),
]
