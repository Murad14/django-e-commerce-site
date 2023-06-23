from django.shortcuts import render
from .models import Products,Order
from django.core.paginator import Paginator
# Create your views here.

def index(req):
    product_objects = Products.objects.all()
    
    #search
    item_name = req.GET.get('item_name')
    if item_name != '' and item_name is not None:
        product_objects = product_objects.filter(title__icontains= item_name)
    
    #paginator
    paginator = Paginator(product_objects,4)
    page = req.GET.get('page')
    product_objects = paginator.get_page(page)
    
    return render(req,'shop/index.html',{'product_objects':product_objects})

def detail(req,id):
    product_object =Products.objects.get(id=id)
    return render(req,'shop/detail.html',{'product_object':product_object})

def checkout(req):
    
    if req.method == "POST":
        name = req.POST.get('name',"")
        email = req.POST.get('email',"")
        address = req.POST.get('address',"")
        city = req.POST.get('city',"")
        state = req.POST.get('state',"")
        zipcode = req.POST.get('zipcode',"")
        
        order = Order(name=name,email=email,address=address,city=city,state=state,zipcode=zipcode)
        order.save()
    
    return render(req, 'shop/checkout.html')
     