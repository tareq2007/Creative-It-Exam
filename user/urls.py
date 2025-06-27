from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.home, name='home'),
    path('add-student/', views.addStudent, name='add-student'),
    path('update-student/<str:pk>/', views.updateStudent, name='update-student'),
    path('delete-student/<str:pk>/', views.deleteStudent, name='delete-student'),
]
