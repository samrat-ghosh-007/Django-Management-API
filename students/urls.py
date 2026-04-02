from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_students),
    path('add/', views.add_student),
    path('edit/<int:id>/', views.update_student),
    path('delete/<int:id>/', views.delete_student),
]