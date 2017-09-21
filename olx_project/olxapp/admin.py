# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from olxapp.models import Category, Advertisement

# Register your models here.

admin.site.register(Category)
admin.site.register(Advertisement)

