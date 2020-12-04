from django.urls import path

from . import views

app_name = 'pub'

urlpatterns = [
    path('', views.public, name='public'),
    #path('listing/', views.listing, name='listing'),
    #path('<int:publication_id>/', views.detail, name='detail'),
    #path('search/', views.search, name='search'),
]