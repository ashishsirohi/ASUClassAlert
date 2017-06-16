# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class userinfo(models.Model):
    username = models.TextField()
    passwd = models.TextField()
    emailid = models.TextField()
    phone = models.BigIntegerField()
    courses = ArrayField(models.BigIntegerField())

class courses(models.Model):
    courseid = models.BigIntegerField()
    term = models.BigIntegerField()
    users = ArrayField(models.BigIntegerField())

