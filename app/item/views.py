from django.shortcuts import render

from .models import Category

def showCat(request):
    return (request,'item/item.html')
