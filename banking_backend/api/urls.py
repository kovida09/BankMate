from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomerInformationViewSet

router = DefaultRouter()
router.register(r'customers', CustomerInformationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
