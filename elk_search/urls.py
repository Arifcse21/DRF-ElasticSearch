# from rest_framework.routers import DefaultRouter
from django.urls import path, include
from elk_search.views import (
    SearchUserViewSet,
    SearchDiscountViewSet,
    SearchProductViewSet,
    SearchCartViewSet,
    SearchProductCategoryViewSet
)


# router = DefaultRouter()
#
# router.register('user', SearchUserViewSet, basename='search-user')
# router.register('product', SearchProductViewSet, basename='search-product')
# router.register('cart', SearchCartViewSet, basename='search-cart')
# router.register('discount', SearchDiscountViewSet, basename='search-discount')


urlpatterns = [
    path('search/user/<str:query>/', SearchUserViewSet.as_view()),
    path('search/product/<str:query>/', SearchProductViewSet.as_view()),
    path('search/category/<str:query>/', SearchProductCategoryViewSet.as_view()),
    path('search/cart/<str:query>/', SearchCartViewSet.as_view()),
    path('search/discount/<str:query>/', SearchDiscountViewSet.as_view()),
]
