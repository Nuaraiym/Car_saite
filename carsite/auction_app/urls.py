from django.urls import path,include
from .views import *
from rest_framework import routers

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


router = routers.DefaultRouter()

router.register(r'users',UserProfileViewSet,basename='users_list'),
router.register(r'brand',BrandViewSet,basename='brand_list'),
router.register(r'car_model',CarModelViewSet,basename='car_model_list'),
router.register(r'car',CarViewSet,basename='car_list'),
router.register(r'auction',AuctionViewSet,basename='auction_list'),
router.register(r'bid',BrandViewSet,basename='bid_list'),
router.register(r'feedback',FeedbackViewSet,basename='feedback_list'),

urlpatterns = [
    path('',include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

