class Queue:
    def __init__(self):
        self.queue = []  # Initialize an empty list to represent the queue

    def enqueue(self, data):
        # Add an element to the end of the queue
        self.queue.append(data)
        print(f"{data} added to the queue.")

    def dequeue(self):
        # Remove and return the first element of the queue
        if len(self.queue) > 0:
            removed_data = self.queue.pop(0)
            print(f"{removed_data} removed from the queue.")
        else:
            print("Queue is empty. Cannot dequeue.")

    def display(self):
        # Display the current elements in the queue
        if len(self.queue) > 0:
            print("Current queue:", self.queue)
        else:
            print("Queue is empty.")

# Function to take user input for operations
def main():
    q = Queue()
    
    while True:
        print("\nQueue Operations:")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Display Queue")
        print("4. Exit")
        
        choice = int(input("Enter your choice (1-4): "))
        
        if choice == 1:
            data = int(input("Enter data to enqueue: "))
            q.enqueue(data)
        elif choice == 2:
            q.dequeue()
        elif choice == 3:
            q.display()
        elif choice == 4:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

# Run the program
if __name__ == "__main__":
    main()
