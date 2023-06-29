from django.shortcuts import render,HttpResponse


# Create your views here.
def index(request):
    context={
        'variable':'this is sent'
    }
    return render(request,'index.html',context)
    
def all_products(request):
    return render(request,'all_products.html')

def deserts(request):
    return render(request,'desert.html')

def contact(request):
    return render(request,'contact_us.html')