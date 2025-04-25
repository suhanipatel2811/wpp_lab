import math
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2)
points = []

for i in range(10):
    x, y, z = map(float, input(f"Enter coordinates of point {i+1} (x y z): ").split())
    points.append((x, y, z))

nearest_neighbors = []


for i in range(10):
    min_dist = float('inf')
    nearest_point = None
    
    for j in range(10):
        if i != j:  
            dist = distance(points[i], points[j])
            if dist < min_dist:
                min_dist = dist
                nearest_point = points[j]
    
    nearest_neighbors.append((points[i], nearest_point))

print("\nList of each point and its nearest neighbor:")
for pair in nearest_neighbors:
    print(f"Point: {pair[0]} -> Nearest Neighbor: {pair[1]}")