from rest_framework import routers

from Order import views

app_name = 'Order'

router = routers.DefaultRouter()
router.register('api/order', views.PlateViewSet, base_name='order')

urlpatterns = router.urls
