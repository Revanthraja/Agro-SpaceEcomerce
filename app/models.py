from django.db import models
from django.contrib.auth.models import User
# Create your models here.

CATEGORY_CHOICES=(
('FR','Fertilizers'),
('FS','FlowerSeeds'),
('VS','VegetableSeeds'),
('PS','Pesticides'),
('PD','Petsfood'),
('WD','Weedicides')

)
STATE_CHOICES=(
("Andaman & Nicobar","Andaman & Nicobar"),
("Andrapradesh","Andrapradesh"),
("Karanataka","Karanataka"),
("Tamil Nadu","Tamil Nadu"),
("Kerala","Kerala"),
("Bihar","Bihar"),
("Telangana","Telangana"),
("Punjab","Punjab"),
("Maharastra","Maharastra"),
("Delhi","Delhi"),
("Gujrat","Gujat"),
("Harayana","Harayana"),
("Goa","Goa"),
("Assam","Assam"),
("Jammu & Kashmir","Jammu & Kashmir "),
("Other","Other"),

)


class Product(models.Model):
    title=models.CharField(max_length=100)
    selling_price=models.FloatField()
    discounted_price=models.FloatField()
    description=models.TextField()
    composition=models.TextField(default='')
    prodapp=models.TextField(default='')
    category=models.CharField(choices=CATEGORY_CHOICES,max_length=2)
    product_image=models.ImageField(upload_to='product')

    def __str__(self):
        return self.title

class Customer(models.Model):
    user=models.ForeignKey(User ,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    locality=models.CharField(max_length=200)
    city=models.CharField(max_length=50)
    mobile=models.IntegerField(default=0)
    zipcode=models.IntegerField()
    state=models.CharField(choices=STATE_CHOICES,max_length=100)

    def __str__(self):
        return self.name
    
class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveBigIntegerField(default=1)

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price
STATUS_CHOICES={

('Accepted',"Accepted"),
('Packed',"Packed"),
('On the way',"on the way"),
('Deliverd',"Deliverd"),
('Cancel',"Cancel"),
('Pending',"Pending")

}



class Payment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    amount=models.FloatField()
    razorpay_order_id=models.CharField(max_length=100,blank=True,null=True)
    razorpay_payment_status=models.CharField(max_length=100,blank=True,null=True)
    razorpay_payment_id=models.CharField(max_length=100,blank=True,null=True)
    paid=models.BooleanField(default=True)




class OrderPlaced(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveBigIntegerField(default=1)
    ordered_date=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=50,choices=STATUS_CHOICES,default='Pending')
    payment=models.ForeignKey(Payment,on_delete=models.CASCADE,default="")
    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price
    

class Wishlist(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)