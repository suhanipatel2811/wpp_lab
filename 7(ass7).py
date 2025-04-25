import math

# Base class for 2D Vector
class Vector2D:
    def __init__(self, x, y):
        self.x = x  # x-coordinate
        self.y = y  # y-coordinate

    def magnitude(self):
        """Returns the magnitude of the vector"""
        return math.sqrt(self.x**2 + self.y**2)

    def rotation(self):
        """Returns the angle of the vector with respect to the X-axis in degrees"""
        return math.degrees(math.atan2(self.y, self.x))

    def distance(self, other):
        """Calculates the distance between two 2D vectors"""
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

    def dot_product(self, other):
        """Calculates the dot product of two 2D vectors"""
        return self.x * other.x + self.y * other.y

    def cross_product(self, other):
        """Calculates the cross product of two 2D vectors (in the 3D space, it's a scalar)"""
        return self.x * other.y - self.y * other.x

# Derived class for 3D Vector (inherits from Vector2D)
class Vector3D(Vector2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)  # Call the constructor of the 2D vector
        self.z = z  # z-coordinate for 3D vector

    def magnitude(self):
        """Returns the magnitude of the 3D vector"""
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def rotation(self):
        """Returns the angle of the 3D vector with respect to the X-axis in degrees"""
        return math.degrees(math.atan2(self.y, self.x))

    def distance(self, other):
        """Calculates the distance between two 3D vectors"""
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2 + (self.z - other.z)**2)

    def dot_product(self, other):
        """Calculates the dot product of two 3D vectors"""
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross_product(self, other):
        """Calculates the cross product of two 3D vectors and returns a new 3D vector"""
        i = self.y * other.z - self.z * other.y
        j = self.z * other.x - self.x * other.z
        k = self.x * other.y - self.y * other.x
        return Vector3D(i, j, k)

# Function to take user input and perform vector operations
def main():
    print("Choose the vector type:")
    print("1. 2D Vector")
    print("2. 3D Vector")
    choice = int(input("Enter your choice (1 or 2): "))

    if choice == 1:
        # 2D vector
        x1 = float(input("Enter the x-coordinate of the first vector: "))
        y1 = float(input("Enter the y-coordinate of the first vector: "))
        x2 = float(input("Enter the x-coordinate of the second vector: "))
        y2 = float(input("Enter the y-coordinate of the second vector: "))
        
        v1 = Vector2D(x1, y1)
        v2 = Vector2D(x2, y2)

        print(f"\nVector 1 Magnitude: {v1.magnitude()}")
        print(f"Vector 1 Rotation: {v1.rotation()} degrees")
        print(f"Distance between vectors: {v1.distance(v2)}")
        print(f"Dot Product: {v1.dot_product(v2)}")
        print(f"Cross Product (2D scalar value): {v1.cross_product(v2)}")

    elif choice == 2:
        # 3D vector
        x1 = float(input("Enter the x-coordinate of the first vector: "))
        y1 = float(input("Enter the y-coordinate of the first vector: "))
        z1 = float(input("Enter the z-coordinate of the first vector: "))
        
        x2 = float(input("Enter the x-coordinate of the second vector: "))
        y2 = float(input("Enter the y-coordinate of the second vector: "))
        z2 = float(input("Enter the z-coordinate of the second vector: "))
        
        v1 = Vector3D(x1, y1, z1)
        v2 = Vector3D(x2, y2, z2)

        print(f"\nVector 1 Magnitude: {v1.magnitude()}")
        print(f"Vector 1 Rotation: {v1.rotation()} degrees")
        print(f"Distance between vectors: {v1.distance(v2)}")
        print(f"Dot Product: {v1.dot_product(v2)}")
        
        cross_prod = v1.cross_product(v2)
        print(f"Cross Product (3D vector): ({cross_prod.x}, {cross_prod.y}, {cross_prod.z})")
    
    else:
        print("Invalid choice. Please choose 1 for 2D vector or 2 for 3D vector.")

# Run the program
if __name__ == "__main__":
    main()
