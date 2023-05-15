from django.urls import path
from . import views

from .views import edit_employee

urlpatterns = [
    path('', views.employees_list, name='employees-list'),
    path('create/', views.create_employee, name='create-employee'),
    path('edit/<int:employee_id>', edit_employee, name='edit-employee'),
    path('delete/', views.delete_employee, name='delete-employee'),
]
