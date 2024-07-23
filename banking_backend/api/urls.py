from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomerInformationViewSet, chat, AccountInformationViewSet, TransactionInformationViewSet, LoanInformationViewSet, CreditCardInformationViewSet

router = DefaultRouter()
router.register(r'customers', CustomerInformationViewSet)
router.register(r'account-information', AccountInformationViewSet)
router.register(r'transaction-information', TransactionInformationViewSet)
router.register(r'loan-information', LoanInformationViewSet)
router.register(r'credit-card-information', CreditCardInformationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('chat/', chat),
]

