from django.shortcuts import render

# Create your views here.
def electronics(request):
    product_dict={
        'heading':'Electronics',
        'product1':'Mac',
        'product2':'IPhone',
        'product3':'Dell'
    }
    return render(request,'productApp/products.html',product_dict)

def toys(request):
    product_dict={
        'heading':'Toys',
        'product1':'Remote Car',
        'product2':'Play Station',
        'product3':'Rocket Launcher'
    }
    return render(request,'productApp/products.html',product_dict)

def shoes(request):
    product_dict={
        'heading':'Shoes',
        'product1':'Nike',
        'product2':'Reebok',
        'product3':'Adidas'
    }
    return render(request,'productApp/products.html',product_dict)

def index(request):
    return render(request,'productApp/index.html')