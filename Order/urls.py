from django.urls import path

from Order import views


urlpatterns = [path('cardapio', views.MenuView.as_view(), name='menu')]
