class Inventory:
    """Class to manage the inventory."""

    def __init__(self):
        self.items = {
            "Laptop": 10,
            "Phone": 20,
            "Headphones": 50,
        }

    def add_item(self, item, quantity):
        """Add new stock to the inventory."""
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")
        self.items[item] = self.items.get(item, 0) + quantity

    def get_stock(self, item):
        """Get the stock of an item."""
        return self.items.get(item, 0)

    def update_stock(self, item, quantity):
        """Update the stock of an item."""
        if item not in self.items:
            raise ValueError(f"Item '{item}' not found in inventory.")
        if quantity > self.items[item]:
            raise ValueError("Insufficient stock.")
        self.items[item] -= quantity


class OrderSystem:
    """Class to handle order processing."""

    def __init__(self, inventory):
        self.inventory = inventory

    def place_order(self, item, quantity):
        """Place an order for a specific item."""
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")
        self.inventory.update_stock(item, quantity)
        return f"Order placed for {quantity} {item}(s)."


