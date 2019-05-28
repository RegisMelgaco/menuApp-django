from rest_framework import routers
from django.urls import path

from Order import views

app_name = 'Order'


router = routers.DefaultRouter()
router.register('api/plate', views.PlateViewSet, base_name='plate')
router.register('api/user', views.UserViewSet, base_name='user')
router.register('api/menu', views.MenuViewSet, base_name='menu')
router.register('api/day_special', views.DaySpecialViewSet, base_name='day_special')
router.register('api/order', views.OrderViewSet, base_name='order')

urlpatterns = router.urls