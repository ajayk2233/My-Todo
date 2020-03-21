from django.urls import path,include
from .views import Todoapi
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('all',Todoapi)

urlpatterns = [
# Default Router route
    path('',include(router.urls)),
]