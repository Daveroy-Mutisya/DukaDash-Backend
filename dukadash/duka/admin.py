from django.contrib import admin
from .models import Merchant, Store, Admin, Clerk, Product, Request, Payment

admin.site.register(Merchant)
admin.site.register(Store)
admin.site.register(Admin)
admin.site.register(Clerk)
admin.site.register(Product)
admin.site.register(Request)
admin.site.register(Payment)
