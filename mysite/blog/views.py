#!/usr/bin/env python
# -*- coding:UTF-8 -*-

from django.shortcuts import render

from django.http import HttpResponse
from blog.diag_end_word import serce

import xlrd

def ajax_demo(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        print(user)
        flag = serce(user)
        flagstr = user+'——————————————'+flag[0] +'\t'+ flag[1] + '\t' + flag[2] + '\t'

        return HttpResponse(flagstr)

    return render(request,'ajax_demo.html')