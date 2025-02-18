from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_data),
    path('add/', views.add_book),
    path('delete/<int:book_id>/', views.delete_book),
    path('edit/<int:book_id>/', views.edit_book)
    
]