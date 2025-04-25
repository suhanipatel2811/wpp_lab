class Node:
    def __init__(self, data):
        self.data = data  # Store data in the node
        self.next = None  # Pointer to the next node, initially set to None

class LinkedList:
    def __init__(self):
        self.head = None  # Initially, the list is empty

    def display(self):
        # Display all elements in the linked list
        if self.head is None:
            print("Linked list is empty.")
            return
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")  # End of the list

    def insert_at_beginning(self, data):
        # Insert a new node at the beginning of the list
        new_node = Node(data)
        new_node.next = self.head  # Point the new node to the current head
        self.head = new_node  # Update the head to the new node

    def insert_at_end(self, data):
        # Insert a new node at the end of the list
        new_node = Node(data)
        if self.head is None:  # If the list is empty
            self.head = new_node
            return
        current = self.head
        while current.next:  # Traverse to the last node
            current = current.next
        current.next = new_node  # Add the new node at the end

    def delete_node(self, key):
        # Delete the first node with the given key (data)
        if self.head is None:
            print("List is empty. Cannot delete.")
            return
        # If the node to be deleted is the head
        if self.head.data == key:
            self.head = self.head.next  # Move the head to the next node
            return
        current = self.head
        while current.next and current.next.data != key:  # Traverse the list
            current = current.next
        # If the key is not found
        if current.next is None:
            print(f"Node with data {key} not found.")
            return
        # Remove the node from the list
        current.next = current.next.next

    def delete_at_beginning(self):
        # Delete the node at the beginning of the list
        if self.head is None:
            print("List is empty. Cannot delete.")
            return
        self.head = self.head.next  # Move the head to the next node

    def delete_at_end(self):
        # Delete the node at the end of the list
        if self.head is None:
            print("List is empty. Cannot delete.")
            return
        # If there is only one node in the list
        if self.head.next is None:
            self.head = None
            return
        current = self.head
        while current.next and current.next.next:  # Traverse to the second last node
            current = current.next
        current.next = None  # Remove the last node


# Function to take user input for operations
def main():
    l = LinkedList()
    
    while True:
        print("\nLinked List Operations:")
        print("1. Insert at Beginning")
        print("2. Insert at End")
        print("3. Delete Node")
        print("4. Delete at Beginning")
        print("5. Delete at End")
        print("6. Display List")
        print("7. Exit")
        
        choice = int(input("Enter your choice (1-7): "))
        
        if choice == 1:
            data = int(input("Enter data to insert at the beginning: "))
            l.insert_at_beginning(data)
        elif choice == 2:
            data = int(input("Enter data to insert at the end: "))
            l.insert_at_end(data)
        elif choice == 3:
            data = int(input("Enter data to delete from the list: "))
            l.delete_node(data)
        elif choice == 4:
            l.delete_at_beginning()
        elif choice == 5:
            l.delete_at_end()
        elif choice == 6:
            l.display()
        elif choice == 7:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")


# Run the program
if __name__ == "__main__":
    main()
