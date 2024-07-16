from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product
from store.models import Customer
from store.models import Collection
# Create your views here.

def say_hello(request):


    product = Product.objects.get(pk=1)

# Customers with .com accounts 
    customers = Customer.objects.all().filter(email__icontains='.com').order_by('-email')

# Collections that don’t have a featured product
    collections = Collection.objects.all().filter(featured_product_id__isnull=True)
# Products with low inventory (less than 10)
# Orders placed by customer with id = 1
# Order items for products in collection 3Solutions are on the next page. codewithmosh.com

    return render(request,'hello.html',
                  {'name': "Roberto", 
                   'customers': customers,
                   'collections': collections
                   })
