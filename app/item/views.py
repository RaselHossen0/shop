from django.shortcuts import render,get_object_or_404

from .models import Category,Item

def showCat(request):
    items=Item.objects.all()
    return (request,'item/item.html',{
        'items':items,
    })
def detail(request,pk):
    item=get_object_or_404(Item,pk=pk)
    return  render(request,'item/detail.html',
           {'item':item},)
