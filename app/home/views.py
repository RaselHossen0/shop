from django.shortcuts import render
def index(request):
    return render(request,'home/fir.html')
def contact(request):
    return render(request,'home/contact.html')