from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views as restview
from olxapp.views import (UserViewSet, AdvertisementViewSet, 
	CategoryViewSet, CategorySearchViewSet, ProductSearchViewSet)


router = routers.DefaultRouter()
router.register(r'user', UserViewSet, 'user_detail')
router.register(r'advertisement', AdvertisementViewSet, 'advertisement')
router.register(r'category', CategoryViewSet, 'category')
router.register(r'categorysearch', CategorySearchViewSet, 'category_search')
router.register(r'productsearch', ProductSearchViewSet, 'product_search')



urlpatterns = [

    url(r'^login/$', restview.obtain_auth_token),

]

urlpatterns += router.urls