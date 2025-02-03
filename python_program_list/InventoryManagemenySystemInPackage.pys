Real-Time Program: Inventory Management System
File Structure

inventory_management/
│
├── inventory_management/
│   ├── __init__.py           # Makes it a package
│   ├── inventory.py          # Module for inventory-related functionality
│   ├── sales.py              # Module for sales-related functionality
│   ├── reporting.py          # Module for reporting-related functionality
│
├── main.py                   # Main program to use the package

Module: inventory.py

Handles inventory operations like adding items and checking stock.

# inventory_management/inventory.py

inventory_data = {}

def add_item(item_name, quantity):
    """Add items to the inventory."""
    if item_name in inventory_data:
        inventory_data[item_name] += quantity
    else:
        inventory_data[item_name] = quantity
    print(f"Added {quantity} of {item_name} to inventory.")

def check_stock(item_name):
    """Check the stock of an item."""
    quantity = inventory_data.get(item_name, 0)
    print(f"Stock of {item_name}: {quantity}")
    return quantity

Module: sales.py

Handles sales operations like selling items.

# inventory_management/sales.py
from .inventory import inventory_data, check_stock

def sell_item(item_name, quantity):
    """Sell an item and update inventory."""
    if item_name not in inventory_data or inventory_data[item_name] < quantity:
        print(f"Error: Not enough stock for {item_name}.")
        return False
    inventory_data[item_name] -= quantity
    print(f"Sold {quantity} of {item_name}.")
    return True

Module: reporting.py

Generates reports for inventory and sales.

# inventory_management/reporting.py
from .inventory import inventory_data

def generate_inventory_report():
    """Generate a report of current inventory."""
    print("\nInventory Report:")
    for item, quantity in inventory_data.items():
        print(f"{item}: {quantity}")
    print()

Main Program: main.py

Demonstrates the usage of the package and its modules.

# main.py
from inventory_management.inventory import add_item, check_stock
from inventory_management.sales import sell_item
from inventory_management.reporting import generate_inventory_report

if __name__ == "__main__":
    print("Welcome to Inventory Management System!\n")
    
    # Add items to inventory
    add_item("Apples", 50)
    add_item("Bananas", 100)
    add_item("Oranges", 75)
    
    # Check stock
    check_stock("Apples")
    check_stock("Bananas")
    
    # Sell items
    sell_item("Apples", 20)
    sell_item("Bananas", 150)  # Insufficient stock
    
    # Generate inventory report
    generate_inventory_report()

