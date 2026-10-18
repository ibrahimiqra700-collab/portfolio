from tkinter.constants import CASCADE

from django.db import models
from django.db.models import ForeignKey, IntegerField


class Product(models.Model):
 name=models.CharField(max_length=50)
 description=models.TextField(blank=True, null=True)
 price=models.DecimalField(max_digits=10,decimal_places=2,default=0)
 image=models.ImageField(upload_to='products/')
 category=models.CharField(max_length=100,default='general')



 def __str__(self):
     return  self.name

class Card(models.Model):
 quantity=models.IntegerField(default=1)
 item=models.ForeignKey(Product,on_delete=models.CASCADE,null=True)

 def __str__(self):
   return self.item.name

class Order(models.Model):
  user=models.CharField(max_length=100)
  phone=models.TextField(blank=True,null=True)
  address=models.TextField(blank=True,null=True)
  item=models.ForeignKey(Product,blank=True,null=True,on_delete=models.CASCADE,related_name="cards")
  quantity=models.IntegerField(default=1)
  price=models.ForeignKey(Product,on_delete=models.CASCADE,related_name="order",null=True,blank=True)
  def __str__(self):
   return f"{self.item}_{self.address}"
class Wishlist(models.Model):
    item=models.ForeignKey(Product,blank=True,null=True,on_delete=models.CASCADE,related_name="wishlist")
    added_at=models.DateTimeField(auto_now_add=True)
def __str__(self):
    return self.item.name


