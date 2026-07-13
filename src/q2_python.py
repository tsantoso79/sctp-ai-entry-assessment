# Question 2 - Arrays and Loops
# Topic: Inventory Tracker
#
# Task 1:
# Declare an empty list called inventory to store item names as strings.

inventory = []


# Task 2:
# Write a function called addItem(itemName) that adds the given item to the
# inventory list. If the item already exists, print a message instead of adding it.
# Example message: "Mouse is already in inventory."

def addItem(itemName):
    """Add itemName to the inventory, skipping (and warning about) duplicates."""
    if itemName in inventory:
        print(f"{itemName} is already in inventory.")
        return

    inventory.append(itemName)


# Task 3:
# Write a function called listInventory() that prints all items in the inventory.
# If the inventory is empty, print: "Inventory is empty."

def listInventory():
    """Print every item in the inventory, or a notice when it is empty."""
    if not inventory:
        print("Inventory is empty.")
        return

    print(f"Inventory: {inventory}")


if __name__ == "__main__":
    # Task 4:
    # Call the functions in this order and observe the output:
    addItem("Laptop")
    addItem("Mouse")
    addItem("Keyboard")
    addItem("Mouse")   # Should trigger duplicate warning
    listInventory()

# Expected output:
# Mouse is already in inventory.
# Inventory: ['Laptop', 'Mouse', 'Keyboard']
