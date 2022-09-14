from django.urls import path
from . import views

urlpatterns = [
    path('createtodo', views.createtodo, name='createtodo'),
    path('alltodos', views.alltodos, name='alltodos'),
    path('deletetodo/<int:id>', views.deletetodo, name='deletetodo'),
    path('detailtodo/<int:id>', views.detailtodo, name='detailtodo'),
    path('edittodo/<int:id>', views.edittodo, name='edittodo'),


    
]