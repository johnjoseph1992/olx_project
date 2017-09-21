# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from django.db.models import F
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from olxapp.serializers import (UserSerializer, 
	AdvertisementSerializer, CategorySerializer)
from olxapp.models import Category, Advertisement
from olxapp.permissions import (UserPermissions, 
	CategoryPermissions, AdvertisementPermissions)

class UserViewSet(viewsets.ModelViewSet):
    """User API view"""
 
    permission_classes = (UserPermissions,)
    serializer_class = UserSerializer
    queryset = User.objects.all()


class AdvertisementViewSet(viewsets.ModelViewSet):
    """Advertisement API view"""

    serializer_class = AdvertisementSerializer
    queryset = Advertisement.objects.all()
    permission_classes = (AdvertisementPermissions,)

    def retrieve(self, request, pk=None):
        queryset = Advertisement.objects.all()
        adverticement_obj = get_object_or_404(queryset, pk=pk)
        Advertisement.objects.filter(pk=pk).update(viewcount=F('viewcount')+1)
        adverticement_obj.viewcount += 1
        serializer_obj = AdvertisementSerializer(adverticement_obj)
        return Response(serializer_obj.data)


class CategoryViewSet(viewsets.ModelViewSet):
    """Category API view"""

    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = (CategoryPermissions,)


class CategorySearchViewSet(viewsets.ModelViewSet):
    """Category search API view"""

    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    filter_backends = (SearchFilter, DjangoFilterBackend,)
    search_fields = ('name',)
    permission_classes = (CategoryPermissions,)


class ProductSearchViewSet(viewsets.ModelViewSet):
    """Product search API view"""

    serializer_class = AdvertisementSerializer
    queryset = Advertisement.objects.all()
    filter_backends = (SearchFilter, DjangoFilterBackend,)
    search_fields = ('name',)
    permission_classes = (AdvertisementPermissions,)



