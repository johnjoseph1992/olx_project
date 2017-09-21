from rest_framework import serializers
from django.contrib.auth.models import User
from olxapp.models import Category, Advertisement


class AdvertisementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Advertisement
        fields = ('category', 'user', 'name', 'price', 'description', 'image', 'posteddate', 'phoneno', 'viewcount')
        read_only_fields = ('viewcount', )


class UserSerializer(serializers.ModelSerializer):

    advertisement_set = AdvertisementSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('username','password','first_name','last_name','email', 'advertisement_set')
        read_only_fields = ('advertisement_set', )


class CategorySerializer(serializers.ModelSerializer):

    advertisement_set = AdvertisementSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ('name', 'advertisement_set')