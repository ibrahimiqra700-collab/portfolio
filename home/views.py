from django.contrib.admindocs.utils import named_group_matcher
from django.contrib.auth import authenticate
from django.shortcuts import render
from . models import Product,Card,Order,Wishlist
from  django.shortcuts import get_object_or_404,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login

# Create your views here.
def  index(request):
    return render(request,"home/index.html")
def newarrivals(request):
    products=Product.objects.all()
    return render(request,"home/newarrivals.html",{'products':products})
def product(request):
    products=Product.objects.all()
    return render(request,"home/product.html",{'products':products})
def card(request):
    cards=Card.objects.all()
    total=0
    for c in cards:
     total+=c.item.price*c.quantity
    print(total)
    return render(request,"home/card.html",{'cards':cards,'total':total})
def delete_card(request,card_id):
    cards=Card.objects.get(id=card_id)
    cards.delete()
    return redirect('card')

def add_to_cart(request,product_id):
    Product_obj=get_object_or_404(Product,id=product_id)
    card_item= Card.objects.filter(item=Product_obj).first()
    if card_item:

      card_item.quantity+=1
      card_item.save()
    else:
      Card.objects.create(
    item=Product_obj,
    quantity=1,
      )


    return redirect('card')

def signup(request):
    if request.method=="POST":
      fullname=request.POST.get('fullname')
      email=request.POST.get('email')
      password=request.POST.get('password')
      confirm_password=request.POST.get('confirm_password')
      if password!=confirm_password:
       print("you enter wrong password")

       return redirect('/')
      else:
        user=  User.objects.create_user(username=fullname,email=email,password=password)
        user.save()
        return  redirect('/login/')
def login(request):
 if request.method=="POST":
     email=request.POST.get('email')
     password=request.POST.get('password')
     user=authenticate(username=email,password=password)

     if user  is not None:
       auth_login(request,user)
       return redirect('/')
     else:
      return redirect('/login/')
 return redirect('/')


def plus(request,card_id):
    card_item=Card.objects.get(id=card_id)
    card_item.quantity+=1
    card_item.save()
    return redirect('card')
def minus(request,card_id) :
    card_item=Card.objects.get(id=card_id)
    if card_item.quantity>1:
     card_item.quantity-=1
     card_item.save()
    else:
         card_item.delete()

    return redirect('card')
def checkout(request):
    if request.method=="POST":
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        address=request.POST.get('address')
        items=Card.objects.all()
        for i in items:
          Order.objects.create(item=i.item,quantity=i.quantity,address=address,phone=phone)

        Card.objects.all().delete()
        return redirect('/thankyou')
    else:
        return render(request,'home/checkout.html')
def thankyou(request):
        return render(request,'home/thankyou.html')
def logout(request):
    logout(request)
    return render('/')
def wishlist(request,pk):
    prod=get_object_or_404( Product,id=pk)
    Wishlist.objects.get_or_create(item=prod)
    return redirect('/wishlistpage')
def wishlistpage(request):
    items=Wishlist.objects.all()
    return render(request,'home/wishlistpage.html',{"items":items})
def wishlist_delete(request,pk):
    wishlist.objects.filter(pk=pk).delete()
    return redirect('/wishlistpage')














            
