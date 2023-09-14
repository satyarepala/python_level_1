"""
**Problem Statement: Inventory Management System**

You are tasked with creating an inventory management system for a retail store. The system should be able to perform
the following operations:

1. **Add Product:** Add a new product to the inventory. Each product has a unique identifier (SKU), a name, a price,
and a quantity in stock.

2. **Remove Product:** Remove a product from the inventory by its SKU.

3. **Update Quantity:** Update the quantity of a product in stock. This operation can be either an increase or a
decrease in quantity.

4. **List Products:** List all products in the inventory, including their SKU, name, price, and quantity in stock.

5. **Calculate Total Value:** Calculate the total value of the inventory, which is the sum of the price of each
product multiplied by its quantity in stock.

6. **Find Products by Price Range:** Find all products within a specified price range (minimum and maximum prices).

Design and implement a Python class `InventoryManager` that can perform these operations efficiently. The class
should have appropriate methods for each operation and maintain an internal data structure to store the products.

Example usage of the `InventoryManager` class:

```python
inventory = InventoryManager()

inventory.add_product("SKU001", "Laptop", 800, 10)
inventory.add_product("SKU002", "Smartphone", 400, 15)
inventory.add_product("SKU003", "Tablet", 300, 20)

inventory.update_quantity("SKU001", 5)
inventory.remove_product("SKU002")

inventory.list_products()
# Output:
# SKU001: Laptop, Price: $800, Quantity: 15
# SKU003: Tablet, Price: $300, Quantity: 20

total_value = inventory.calculate_total_value()
print(f"Total Inventory Value: ${total_value}")

products_in_range = inventory.find_products_by_price_range(200, 500)
print("Products in Price Range (200-500):")
for product in products_in_range:
    print(f"{product['sku']}: {product['name']}, Price: ${product['price']}, Quantity: {product['quantity']}")
```

Implement the `InventoryManager` class to meet these requirements and ensure that it handles edge cases such as
invalid SKU, negative quantity, and other potential errors gracefully.
 """
class Product:
    def __init__(self, sku, name, price, quantity):
        self.sku = sku
        self.name = name
        self.price = price
        self.quantity = quantity

class InventoryManager:
    def __init__(self):
        self.inventory = {}

    def add_product(self, sku, name, price, quantity):
        if sku not in self.inventory:
            self.inventory[sku] = Product(sku, name, price, quantity)
        else:
            print(f"Product with SKU {sku} already exists.")

    def remove_product(self, sku):
        if sku in self.inventory:
            del self.inventory[sku]
        else:
            print(f"Product with SKU {sku} does not exist.")

    def update_quantity(self, sku, quantity_change):
        if sku in self.inventory:
            self.inventory[sku].quantity += quantity_change
        else:
            print(f"Product with SKU {sku} does not exist.")

    def list_products(self):
        for product in self.inventory.values():
            print(f"{product.sku}: {product.name}, Price: ${product.price}, Quantity: {product.quantity}")

    def calculate_total_value(self):
        total_value = sum(product.price * product.quantity for product in self.inventory.values())
        return total_value

    def find_products_by_price_range(self, min_price, max_price):
        products_in_range = []
        for product in self.inventory.values():
            if min_price <= product.price <= max_price:
                products_in_range.append({
                    'sku': product.sku,
                    'name': product.name,
                    'price': product.price,
                    'quantity': product.quantity
                })
        return products_in_range

# Example usage
inventory = InventoryManager()

inventory.add_product("SKU001", "Laptop", 800, 10)
inventory.add_product("SKU002", "Smartphone", 400, 15)
inventory.add_product("SKU003", "Tablet", 300, 20)

inventory.update_quantity("SKU001", 5)
inventory.remove_product("SKU002")

inventory.list_products()

total_value = inventory.calculate_total_value()
print(f"Total Inventory Value: ${total_value}")

products_in_range = inventory.find_products_by_price_range(200, 500)
print("Products in Price Range (200-500):")
for product in products_in_range:
    print(f"{product['sku']}: {product['name']}, Price: ${product['price']}, Quantity: {product['quantity']}")
