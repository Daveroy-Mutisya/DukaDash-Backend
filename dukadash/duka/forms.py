from django import forms
from .models import Store, Merchant,Admin, Clerk, Payment,Request,Product


class MerchantForm(forms.ModelForm):
    class Meta:
        model = Merchant
        fields = ('name', 'email', 'password', 'phone_number', 'address')

class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ['name', 'location', 'image', 'merchant', 'admin', 'clerk']


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Admin,Clerk
        admin_fields = ['name', 'email', 'image','phone_number', 'password']
        clerk_fields = ['name', 'email', 'image','phone_number', 'password','sales_made']

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['store', 'status','date','amount','method','due_date']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','image','price','condition','stock_quantity','spoil_quantity','buying_price','selling_price',]

class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['store','product','quantity','requester_name','requester_contact','status']

