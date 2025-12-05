from django.urls import path
from . import views

app_name = 'popularity'

urlpatterns = [
    path('', views.popularity_map, name='map'),
    path('<int:region_id>/', views.region_detail, name='region_detail'),
]
