# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Advertisement(models.Model):
    category = models.ForeignKey(Category, models.CASCADE)
    user = models.ForeignKey(User, models.CASCADE)
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to="olxapp/imgs")
    posteddate = models.DateTimeField(auto_now_add=True)
    viewcount = models.IntegerField(default=0)
    phoneno = models.CharField(max_length=15, null=True)

    def __str__(self):
        return self.name
