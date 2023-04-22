from django.urls import path
from todoapp.views import index, add_item, delete, turn_On, turn_Off, add_user, account

urlpatterns = [
    path('', index, name='index'),
    path('add/', add_item, name='add'),
    path('delete/<item>/', delete, name='delete'),
    path('account/', account, name='account'),
    path('add_user/', add_user, name = 'add_user'),
    path('turn_On/<item>/', turn_On, name='turn_On'),
    path('turn_Off/<item>/', turn_Off, name='turn_Off'),
]