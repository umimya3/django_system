from django.urls import path
from . import views

app_name = 'schedule'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:event_id>/', views.detail, name='detail'),
    path('<int:event_id>/vote/<int:candidate_id>/', views.vote, name='vote'),
]
