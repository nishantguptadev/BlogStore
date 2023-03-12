from django.shortcuts import render
from .models import *
from math import ceil
import json
from django.contrib import messages

# Create your views here.
def index(request):
    allProds=[]
    catprods= Product.objects.values('category', 'id')
    cats={item['category'] for item in catprods}
    for cat in cats:
        prod=Product.objects.filter(category=cat)
        n=len(prod)
        
        nSlides = n// 4 + ceil((n/4)- (n//4))
        allProds.append([prod, range(1,nSlides), nSlides])
    params={'allProds':allProds}
    return render(request, "store/index.html", params)

def cart(request):
    return render(request, "store/cart.html")

def searchMatch(query, item):
    if query in item.name.lower() or query in item.desc.lower() or query in item.category.lower():
        return True

def search(request):
    query=request.GET.get("search")
    allProds=[]
    allprodtemp=[]
    catprods= Product.objects.values('category', 'id')
    cats={item['category'] for item in catprods}
    for cat in cats:
        prodtemp=Product.objects.filter(category=cat)
        # prod=[item for item in prodtemp if query in item.desc] or
        prod=[item for item in prodtemp if  searchMatch (query, item)] # function is above for it
        n=len(prod)
        nSlides = n// 4 + ceil((n/4)- (n//4))
        allprodtemp.append([prodtemp, range(1,nSlides), nSlides])
        if len(prod) != 0:
            allProds.append([prod, range(1,nSlides), nSlides])
        
        params={
            'allProds':allProds,
            'allprodtemp':allprodtemp
        }
    if len(allProds) == 0:
        messages.info(request,"Please enter relevent query")
        
        return render(request, "store/search.html", params)
    return render(request, "store/search.html", params)


def checkout(request):
    
    if request.method=="POST":
        items_json=request.POST.get('itemsJson','') #itemJson is the id given in html
        name=request.POST.get('name', '')
        amount=request.POST.get('amount', '')
        email=request.POST.get('email', '')
        address=request.POST.get('address', '')
        city=request.POST.get('city', '')
        state=request.POST.get('state', '')
        zip_code=request.POST.get('zip_code', '')
        phone=request.POST.get('phone', '')
        order=Order(name=name, email=email, items_json=items_json, address=address, city=city,state=state, zip_code=zip_code,phone=phone, amount=amount)
        order.save()
        # update= OrderUpdate(order_id=order.order_id, update_desc="The order has been placed")#to update tracker
        # update.save()
        thank=True
        id= order.order_id
        return render(request,"store/checkout.html",{'thank': thank,'id':id})
    return render(request,"store/checkout.html")

def productView(request, myid):
    product=Product.objects.filter(id=myid)
    print(product)
    return render(request,'store/prodView.html',{'product': product[0]})