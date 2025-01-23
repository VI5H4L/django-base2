THINGS LEARNT

--------------------------------------------------------------------------------

CBVs - Create,Update,Delete,Form Views

--------------------------------------------------------------------------------

form.as_table
form.as_p
form.as_ul

--------------------------------------------------------------------------------

Reverse vs ReverseLAZY :

reverse: Resolves the URL immediately and returns a string. Use it in views, models, and places where the URL is required at runtime.

reverse_lazy: Delays URL resolution until accessed. Use it in class-based view attributes, settings, and any scenario where early resolution might cause issues.

--------------------------------------------------------------------------------

Creating Custom fields:

UppercaseCharField on top of Charfield to save data on DB in uppercase

--------------------------------------------------------------------------------

Using Django ORM, Aggregations, and Q Objects:

from customapp.models import Product
from django.db.models import Q, Avg, Sum, Max, Min

# Create Products
Product.objects.create(name="Laptop", description="A powerful laptop", price=1000.00, stock=10)
Product.objects.create(name="Monitor", description="A 4K monitor", price=300.00, stock=20)

# Retrieve All Products
products = Product.objects.all()

# Filter with Q objects
expensive_products = Product.objects.filter(Q(price__gte=500) | Q(stock__lt=15))

# Aggregations
average_price = Product.objects.aggregate(Avg('price'))
total_stock = Product.objects.aggregate(Sum('stock'))

print(f"Average Price: {average_price}")
print(f"Total Stock: {total_stock}")

# Create a product
product = Product.objects.create(name="smartphone", description="A high-end phone", price=800.00, stock=5)
print(product.name)  # Output: SMARTPHONE (converted to uppercase)

--------------------------------------------------------------------------------

fake migrations for manual adjustments and database synchronization

Fake a migration (without running it):
python manage.py migrate <app_name> --fake

Fake a specific migration:
python manage.py migrate <app_name> <migration_name> --fake

Undo migrations to a specific migration:
python manage.py migrate <app_name> <previous_migration_name>

Undo all migrations for an app:
python manage.py migrate <app_name> zero

Apply all migrations:
python manage.py migrate

Check migration status:
python manage.py showmigrations

--------------------------------------------------------------------------------