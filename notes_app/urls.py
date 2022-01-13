
from django.urls import path
from notes_app import views
from notes_app.models import Notes

urlpatterns = [
    path('index/', views.index, name='index'),
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('mark_complete/<int:id>', views.mark_complete, name='mark_complete'),
]
