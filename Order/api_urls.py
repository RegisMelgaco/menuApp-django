from rest_framework import routers
from django.urls import path

from Order import views

app_name = 'Order'


router = routers.DefaultRouter()
router.register('plate', views.PlateViewSet, base_name='plate')
router.register('user', views.UserViewSet, base_name='user')
router.register('menu', views.MenuViewSet, base_name='menu')
router.register('day_special', views.DaySpecialViewSet, base_name='day_special')
router.register('order', views.OrderViewSet, base_name='order')


urlpatterns = router.urls
