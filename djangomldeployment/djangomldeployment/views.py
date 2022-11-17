# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 15:50:03 2022

@author: kiran
"""


import pickle

import project 
from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request,"head.html" )
def result(request ):
    
    ap=pickle.load(open('model.pkl','rb'))
    lis = []
    lis.append(int(request.GET["1st"]))
    lis.append(int(request.GET['2nd']))
    lis.append(int(request.GET['3rd']))
    lis.append(int(request.GET['4th']))
    lis.append(int(request.GET['5th']))
    lis.append(int(request.GET['6th']))
    lis.append(int(request.GET['7th']))
    lis.append(int(request.GET['8th']))
    lis.append(int(request.GET['9th']))
    lis.append(int(request.GET['10th']))
    lis.append(int(request.GET['11th']))
    lis.append(int(request.GET['12th']))
    lis.append(int(request.GET['13th']))
    lis.append(int(request.GET['14th']))
    lis.append(int(request.GET['15th']))
    lis.append(int(request.GET['16th']))
    lis.append(int(request.GET['17th']))
    lis.append(int(request.GET['18th']))
    lis.append(int(request.GET['19th']))
    lis.append(int(request.GET['20th']))
    
    ans = ap.predict([lis]) 
    return render(request,"result.html", {'ans':ans})