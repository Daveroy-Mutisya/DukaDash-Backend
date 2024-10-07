from django.shortcuts import render, redirect
import requests
import json
from . models import Store,Merchant,Admin,Clerk,Payment,Request,Product
from .forms import StoreForm, EmployeeForm
# Create your views here.

class Stores:
 def store_list(request):
    store = Store.objects.all()
    return render(request,'store_list.html',{'store':store})
 
 def add_store(request):
   if request.method == 'POST':
     form = StoreForm(request.POST)
     if form.is_valid():
       form.save
       return redirect('store_list')
     else :
       form = StoreForm()
   
   return render(request,'store/add_store.html',{'form':form})
 
class Employees:
 def employee_list (request):
    admin = Admin.objects.all()
    clerk = Clerk.objects.all()
    return render(request,'employee_list.html',{'admin':admin,'clerk':clerk})
 
 def add_employee(request):
   if request == 'POST':
     form = EmployeeForm(request.POST)
   if form.is_valid():
       form.save
       return redirect('employees_list')
   else :
     form = EmployeeForm
     return render(request,'employee/add_employee.html',{'form':form})

class Products:
 def products_list (request):
    products = Product.objects.all()
    return render(request,('products_list.html',{'products' :products}))

class Payements:
 def payment_list(request):
    payments = Payment.objects.all()
    return render (request, ('payments_list.html',{'payments' :payments}))

class Requests:
 def request_list(request):
    requests = Request.objects.all()
    return render (request, ('requests_list.html',{'requests' :requests}))
 
#  def send_register(request):
#    if request =='POST':
     
class Merchants:
 def merchant_list(request):
    merchant = Merchant.objects.all()
    return render (request,{'merchant_list.html',{'merchant': merchant}})
 
def signup_merchant(request):
   if request.method == 'POST':
       merchant = Merchant.objects.create()
       merchant.save()
       return redirect('login')
   else:
     return f"Error registering Merchant"
   



    

