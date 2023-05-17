from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
from .forms import *

# Create your views here.
def add_product(request):
    Product = product.objects.filter()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("shop")
            # Redirect to a success page or perform any additional logic
    else:
        form = ProductForm()
    context = {
            'Product':Product,
            'form' : form
    }
    return render(request,'add.html', context)
def shop(request):
    Product = product.objects.filter()
    context = {'Product':Product}
    return render(request,'shop.html', context)

def shopview(request, name):
    if(product.objects.filter(name=name)):
        Product = product.objects.filter(name=name).first()
        Random = product.objects.all().order_by('?')[:4]
        context = {'Product':Product,'Random':Random}
        return render(request,'sproduct.html', context)
    else:
        messages.warning(request, "No such producy found")
        return redirect('shop')
    
def product_update(request, pk):
    products = product.objects.get(id=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST or None, instance = products)
        if form.is_valid():
            form.save()
            return redirect("shop")
    else:
        form = ProductForm(instance = products)
    context = {
            'form' : form
    }
    return render(request, 'update_prod.html',context)

def shop_delete(request, pk):
    item = product.objects.filter(id=pk)
    if request.method == 'POST':
        if(item):
            item.delete()
        return redirect('shop')
    context = {
        'item' : item,
    }
    return render(request, 'prod_delete.html',context)