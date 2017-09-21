from rest_framework import permissions
from rest_framework import authentication
from olxapp.models import Category, Advertisement


class UserPermissions(permissions.IsAuthenticated):

    def has_permission(self, request, view):

        if request.user.is_authenticated:
            return True
        if request.method in ('POST'):
            return True

    def has_object_permission(self, request, view, obj):
        if obj== request.user or request.user.is_superuser:
            return True


class CategoryPermissions(permissions.IsAuthenticated):

    def has_permission(self, request, view):

        if request.user.is_superuser:
            return True
        if request.method in ('GET'):
            return True


    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        else:
            if request.method in ('GET'):
                return True
            return False


class AdvertisementPermissions(permissions.IsAuthenticated):

    def has_permission(self, request, view):

        if request.user.is_authenticated:
            return True
        if request.method in ('GET'):
            return True


    def has_object_permission(self, request, view, obj):
        if obj.user == request.user or request.user.is_superuser:
            return True
        else:
            if request.method in ('GET'):
                return True
            return False