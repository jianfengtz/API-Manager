from django.db import models

# Create your models here.
# -*- coding: utf-8 -*-
class ApiCaches(models.Model):
    username = models.CharField(max_length=32)
    apiname = models.CharField(max_length=32)
    timeid = models.CharField(max_length=32)
    content = models.TextField()
