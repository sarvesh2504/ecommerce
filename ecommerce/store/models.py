from django.db import models

# Create your models here.
# product.

from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
#category.

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

#customer.

from django.db import models
from django.contrib.auth.models import AbstractUser

class Customer(AbstractUser):
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    email = models.EmailField(unique=True)

    # Specify unique related_name arguments for groups and user_permissions
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customer_groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customer_user_permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def __str__(self):
        return self.username

#order.

from django.db import models
from store.models import Product

class Order(models.Model):
    customer = models.ForeignKey('store.Customer', on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='OrderItem')
    order_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order #{self.pk} - {self.customer.username} - {self.order_date}"
    
#order-item.
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} x {self.product.name} ({self.order})"

#cart.
from django.db import models
from store.models import Product

class Cart(models.Model):
    customer = models.ForeignKey('store.Customer', on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='CartItem')

    def total_price(self):
        return sum(item.product.price * item.quantity for item in self.cartitem_set.all())

    def __str__(self):
        return f"Cart for {self.customer.username}"
    
#cart-item.
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def subtotal(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f"{self.quantity} x {self.product.name} in cart for {self.cart.customer.username}"

#address.
from django.db import models
from store.models import Customer

class Address(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='addresses')
    address_line1 = models.CharField(max_length=255)
    address_line2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.customer.username} - {self.address_line1}, {self.city}, {self.state} {self.postal_code}"

#payment.
from django.db import models
from store.models import Order

class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    payment_date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50)
    # Add more fields as needed for payment information

    def __str__(self):
        return f"Payment for Order #{self.order.pk} - {self.payment_date}"




