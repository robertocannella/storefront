from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.

class Collection(models.Model):
    title = models.CharField(max_length=255)
    featured_product = models.ForeignKey('Product',on_delete=models.SET_NULL,null=True, related_name='+')
    
    def __str__(self) -> str:
        return self.title
    
    class Meta():
        ordering = ['title']
  

class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()

class Product(models.Model):
    #  Custom Primary Key:
    #  product_id = models.CharField(max_length=15, primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    slug = models.SlugField()
    unit_price = models.DecimalField(
        max_length=100,
        max_digits=10, 
        decimal_places=3, 
        validators=[
            MinValueValidator(1)
        ])
    inventory = models.IntegerField(validators=[
        MinValueValidator(0)
    ])
    last_update = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT)
    promotions = models.ManyToManyField(Promotion, blank=True)

    def __str__(self) -> str:
        return self.title
    
    class Meta():
        ordering = ['title']

class Customer(models.Model):
    MEMBERSHIP_GOLD = 'G'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_BRONZE = 'B'

    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_GOLD, 'Gold'),
        (MEMBERSHIP_SILVER, 'Silver'),
        (MEMBERSHIP_BRONZE, 'Bronze'),
    ]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_1 = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
    membership = models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_BRONZE)

    def __str__(self) -> str:
        return f'{self.last_name}, {self.first_name}'

    class Meta():
        indexes = models.Index(fields=["last_name", "first_name"]),
        ordering = ['last_name', 'first_name']
class Order(models.Model):
    PAYMENT_STATUS_PENDING = 'P'
    PAYMENT_STATUS_COMPLETE = 'C'
    PAYMENT_STATUS_FAILED = 'F'

    PAYMENT_STATUS_CHOICES = [
        (PAYMENT_STATUS_PENDING, 'Pending'),
        (PAYMENT_STATUS_COMPLETE, 'Completed'),
        (PAYMENT_STATUS_FAILED, 'Failed')
    ]

    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=1, choices=PAYMENT_STATUS_CHOICES, default=PAYMENT_STATUS_PENDING)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    
    class Meta():
        ordering = ['placed_at']

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT, null=True)
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=10,decimal_places=3)

class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=10, null=True)
    # For One to One relationship
    # Specify Parent
    # customer = models.OneToOneField(Customer, on_delete=models.CASCADE, primary_key=True)

    # For One to Many relationship
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

class Cart(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()
