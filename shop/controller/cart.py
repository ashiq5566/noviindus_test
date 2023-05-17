from django.http.response import JsonResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from shop.models import *
from django.contrib.auth.decorators import login_required
import random


def addtocart(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            prod_id = int(request.POST.get('product_id'))
            prod_qty = int(request.POST.get('product_qty')) 
            product_check = product.objects.get(id=prod_id)
            if(product_check):
                if(cart.objects.filter(user=request.user.id,product_id=prod_id)):
                    return JsonResponse({'status':"Product Already in Cart"})
                else:
                    if prod_qty <= 0 or prod_qty > 10:
                        return JsonResponse({'status':"Choose the quantity Between 1 - 10"})
                    else:
                        if product_check.quantity >= prod_qty:
                            cart.objects.create(user=request.user,product_id=prod_id,product_qty=prod_qty)
                            return JsonResponse({'status':"Product Added Successfully"})
                        else:
                            return JsonResponse({'status':"Only "+ str(product_check.quantity) + " quantity available"})         
            else:
                return JsonResponse({'status':"No such product found"})
        else:
            return JsonResponse({'status':"Login Required"})
    return redirect('/')
            

@login_required(login_url='register')
def viewcart(request):
    Cartlist = cart.objects.filter(user=request.user)
    total_price = 0
    for item in Cartlist:
        total_price = total_price + item.product.price * item.product_qty

    shipping = 50
    total = total_price + shipping
    context = {'Cartlist':Cartlist, 'total_price':total_price,'total':total}

    if request.method == "POST":
        product_id = request.POST.get('prod_id')
        product_qty = request.POST.get('prod_qty')
        cartitem = cart.objects.filter(user=request.user, product_id=product_id, product_qty=product_qty)
        if(cartitem):
            cartitem.delete()
            return redirect('cart')
    return render(request,"cart.html", context)