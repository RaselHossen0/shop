from django.shortcuts import render
from item.models import Category,Item
def index(request):
     items=Item.objects.all()
     categoris=Category.objects.all()
   
     return render(request,'home/fir.html',{
        'items':items,'categories':categoris,
    })
def contact(request):
   
    return render(request,'home/contact.html')