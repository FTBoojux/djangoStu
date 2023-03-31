from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('users', views.list_user, name='users'),
    path('user/<int:id>/', views.get_user_by_id, name='user')
]