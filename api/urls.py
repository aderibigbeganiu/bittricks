from django.urls import path, include
from rest_framework import routers
from users.views import UserViewSet
from orders.views import OrderViewSet



router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'orders', OrderViewSet)



urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),

]