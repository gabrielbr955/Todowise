from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='app_index'),
    path('login/', views.app_login, name='app_login'),
    path('logout/', views.app_logout, name='app_logout'),
    path('list/<int:list_id>', views.todo_list, name='todo_list'),
    path('list/<int:list_id>/add', views.add_item, name='add_item'),
    path('list/<int:list_id>/remove/<int:item_id>/', views.remove_item, name='remove_item')
]
