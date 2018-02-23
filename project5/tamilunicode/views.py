# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from tamilunicode.models import *
from string import letters

# Create your views here.
def unicodes(request):
    letters = []
    if "word" in request.GET:
        letter_list = list(request.GET["word"])
            unicode = TamilUnicode.objects.get(letter__contains=l)
            letters.append(unicode)
    else:
        return "not found"
    data = {}
    
    data["letters"] = letters
    
    return render(request, 'tam_unicode.html', data)