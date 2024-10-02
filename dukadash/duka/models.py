from django.db import models

# Create your models here.

class Merchant (models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=20)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    image = models.CharField(max_length=300, blank=True, null=True)
    description = models.TextField(max_length=500)

    def __str__(self) -> str:
        return super().__str__() + self.name
    
class Store (models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    image = models.CharField(max_length=300, blank=True, null=True)
    location = models.CharField(max_length=75)
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE)
    admin = models.ForeignKey('Admin', on_delete=models.SET_NULL, null=True, blank=True)
    clerk = models.ForeignKey('Clerk', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name
    
class Admin(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=20)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    image = models.CharField(max_length=300, blank=True, null=True)
    description = models.TextField(max_length=500)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return super().__str__() + self.name
    
class Clerk (models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=20)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    image = models.CharField(max_length=300, blank=True, null=True)
    description = models.TextField(max_length=500)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return super().__str__() + self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    image = models.CharField(max_length=255, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    condition = models.CharField(max_length=50)
    stock_quantity = models.IntegerField()
    spoil_quantity = models.IntegerField()
    buying_price = models.DecimalField(max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Request(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    requester_name = models.CharField(max_length=255)
    requester_contact = models.CharField(max_length=20)
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"Request from {self.requester_name} for {self.product.name}"

class Payment(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    date = models.DateTimeField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    method = models.CharField(max_length=50)
    due_date = models.DateField()

    def __str__(self):
        return f"Payment of {self.amount} for {self.store.name}"
