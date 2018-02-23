# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class TamilUnicode(models.Model):
    unicode = models.CharField(max_length=10)
    letter = models.CharField(max_length=5)
    description = models.CharField(max_length=25)
    
    class Meta:
        ordering = ['id']
    def __str__(self):
        return str(self.unicode)