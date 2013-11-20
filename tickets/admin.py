__author__ = 'prikozhd'
# -*- coding: utf-8 -*-
from django.contrib import admin
from models import Departament


class AdminDepartament(admin.ModelAdmin):
    search_fields = ['locale', 'name']
    list_filter = ['locale', 'name']


admin.site.register(Departament, AdminDepartament)
