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