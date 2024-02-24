from django.contrib import admin

# Register your models here.
# product.
from django.contrib import admin
from .models import Product

admin.site.register(Product)

# category.
from django.contrib import admin
from .models import Category

admin.site.register(Category)

# customer.
from django.contrib import admin
from .models import Customer

admin.site.register(Customer)

#order.
from django.contrib import admin
from .models import Order

admin.site.register(Order)

#order-item.
from django.contrib import admin
from .models import OrderItem

admin.site.register(OrderItem)

#address.
from django.contrib import admin
from .models import Address

admin.site.register(Address)

#payment.
from django.contrib import admin
from .models import Payment

admin.site.register(Payment)


