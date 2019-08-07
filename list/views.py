from django.shortcuts import render
from .models import test

# Create your views here.
def home(request):
      
    return render(request,'index.html',)


def list(request):
     
    a = test.objects.order_by('name') 
    return render(request,'list.html',{'list':a})