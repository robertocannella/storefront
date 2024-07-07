# Setup Project

## Configure Environment
1. Project Directory
    
    Create the project directory and then navigate to that directory.  This can be done within any directory:

    ```
    mkdir storefront
    cd storefront
    ```
2. Create Virtual Environment

    Use `vitualenv` to create an virtual python environment. Then activate the environment:

    ```
    virtualenv venv
    source venv/bin/activate
    ```
3. Install Django within the virtual environment.

    Install Django and create a new project (notice trailing period `.`):
    ```
    pip install django
    django-admin startproject storefront .
    ```
4. Run the Django Dev server (with app settings):


    **With app settings:** (use this one)
    ```
    python3 manage.py runserver
    ```
    Without app settings:
    ```
    django-admin runserver
    ```

## Install Debugger

Follow the instructions here:

* https://django-debug-toolbar.readthedocs.io/en/latest/installation.html

* TODO: Detail out this process.
    * `pip install django-debug-toolbar`
* TODO: Detail out launch.json config.


## Create App(s)
1. Create `store` and `tag` apps:

    ```
    python3 manage.py startapp store
    python3 manage.py startapp tag
    ```
2. Add app(s) to `settings.py`

    ```
    INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    ...
    'debug_toolbar',
    'store',
    'tag'
    ]
    ```
## Create Models
Add models to`models.py`
```

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=3)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)

```

## Database Setup:
### One To One Relationships
Create a One-To-One relationship between Customers and Addresses.  Each customer has only one address and each address belongs to only one customer.

Add an `Address` class to `models.py`

```
class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    # Specify Parent
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, primary_key=True)
```

### One To Many Relationships
Allow Customers to have multiple address.

Amend the `Address` class in `models.py`

```
class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    
    # For One to One relationship
    # Specify Parent
    # customer = models.OneToOneField(Customer, on_delete=models.CASCADE, primary_key=True)

    # For One to Many relationship
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
```

Do the same for: 
* Collection - Product 
* Customer - Order
* Order - Item
* Cart - Item

### Many To Many Relationships
Create a many-to-many relationship between Promotions and Products. A Promotion can have many Products and a Product and belong to many Promotions:

Add a `Promotion` class to `models.py` and reference it in the Product Class.  There is no need to create the reverse reference in the `Promotion` class.  It will be auto generated by Django. The column name defaults to `product_set`.  
```
class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()

class Product(models.Model):
    #  Custom Primary Key:
    #  product_id = models.CharField(max_length=15, primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=3)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT)
    promotions = models.ManyToManyField(Promotion)
```
### Circular Relationships
A circular relationship exists between Product and Collection.  A collection has a `featured_product` (Product foreign-key reference) and a Product has a `collection` (Collection foreign key reference).

Since the Product class is defined in `models.py` after the Collection class, wrap the Product class name in single quotes `'Product'`. Also, set related_name to '+' for django to ignore this field. 
```
class Collection(models.Model):
    title = models.CharField(max_length=255)
    featured_product = models.ForeignKey('Product',on_delete=models.SET_NULL,null=True, related_name='+')

```
### Generic Relationships

To create generic relationship types between apps, for instance, Tags and Products or Likes and Users, add the following fields:
* content_type
* object_id
* content_object

Additionally, import the referenced classes.

```
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.
class Tag(models.Model):
    label = models.CharField(max_length=255)

class TagItem(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    # Generic Type
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveBigIntegerField()
    content_object = GenericForeignKey()
```
### Migrations
#### Make Migrations

To make migrations, run this command.
`python3 manage.py makemigrations`

*note*: verify all apps with migrations are listed in `settings.py` under the INSTALLED_APPS list.

#### Run Migrations
To run migrations (create tables) for the currently configured database run:
`python3 manage.py migrate`

Additionally, this command shows sql command:
`python3 manage.py sqlmigrate store 0001_initial`

*note*: this results of the `sqlmigrate` are dependent on the database engine.

#### Reverting Migrations

Best to use version control to undo migrations. 

This command will set the migration level:
`python3 manage.py migrate store 0005`

### Customize Schema



Use an inner class called Meta to customize schema:

```

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

    class Meta:
        indexes = models.Index(fields=["last_name", "first_name"]),

```

more options for schema customization are here:

https://docs.djangoproject.com/en/5.0/ref/models/options/


### Install MYSQL Connector

`pip install mysqlclient`

configure database in `settings.py`

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'storefront',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': ''
    }
}
```

Run migrations:
`python3 manage.py migrate`

### Custom SQL:

Create an empty migration:

`python3 manage.py makemigrations store --empty`


Add Upgrade and Downgrade SQL commands in the `RunSQL` function

```
class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_customer_store_custo_last_na_2e448d_idx'),
    ]

    operations = [
        migrations.RunSQL("""
            INSERT INTO store_collection (title)
                VALUES ('collection1')
        """,
        """
            DELETE FROM store_collection 
                WHERE title = 'collection1';
        """
                          )
    ]
```

### Generate Dummy Data

https://mockaroo.com/

Create data, download and run sql against database.

## Django ORM

https://docs.djangoproject.com/en/5.0/ref/models/querysets/

# Admin Site

Accessible through url /admin

## Configuration

### Create user:

`python3 manage.py createsuperuser`

### Update password:

`python3 manage.y changepassword <user>`

### Customize Headings:
In the project `urls.py` file:

```
from django.contrib import admin
from django.urls import path, include
from debug_toolbar.toolbar import debug_toolbar_urls

admin.site.site_header = 'Storefront Admin'
admin.site.index_title = 'Admin'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('playground/', include('playground.urls'))
] + debug_toolbar_urls()
```

## Register Models
In the APP `admin.py` file, register the model:

```
from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Collection)
```

### Update _str__ 
Overwrite the magic `__str__` method to change the string representation of an object.  This is for better readability in the admin site listing of the Model.  

Additionally, add a Meta class for sorting.

```
class Collection(models.Model):
    title = models.CharField(max_length=255)
    featured_product = models.ForeignKey('Product',on_delete=models.SET_NULL,null=True, related_name='+')
    
    def __str__(self) -> str:
        return self.title
    
    class Meta():
        ordering = ['title']
```
## Model Admin
https://docs.djangoproject.com/en/5.0/ref/contrib/admin/#modeladmin-objects

```
from django.contrib import admin
from . import models

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [ 'title' , 'unit_price']
    list_editable = ['unit_price']
    list_per_page  = 10

# Register your models here.
admin.site.register(models.Collection)

```
