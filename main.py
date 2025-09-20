import heapq
import time

class RoadMap:
    def __init__(self):
        self.adjacency_list = {} # Weighted Adjacency list representation of the graph

    def addRoad(self, from_city, to_city, distance):
        if from_city == to_city: # No self-loops
            return
        if (to_city, distance) in self.adjacency_list.get(from_city, []): # No duplicate edges
            return
        if from_city not in self.adjacency_list: # Initialize list if city not present
            self.adjacency_list[from_city] = []
        self.adjacency_list[from_city].append((to_city, distance))
        self.addRoad(to_city, from_city, distance) # Undirected graph, add both ways

    def printMap(self):
        print("-------------\nPrint Roadmap\n-------------")
        for city, roads in self.adjacency_list.items(): # loop through each city and its neighbors
            print(f"{city}: {roads}")

    def bfs(self, start, destination): # O(V + E) time complexity, O(V) space complexity
        print("-------------------------\nBreadth First Search Path\n-------------------------")
        visited = set() # Track visited cities
        queue = [(start, 0)] # (city, distance)

        while queue: 
            current, distance = queue.pop(0)
            print(f"{current} (distance: {distance})", end=" ->\n") 
            if current == destination: # destination check
                print(f"Total Distance: {distance}")
                return
            if current not in visited: # if city not visited, mark as visited and add neighbors to queue
                visited.add(current)
                for neighbor, ndistance in self.adjacency_list[current]:
                    if neighbor not in visited:
                        queue.append((neighbor, distance + ndistance))
        
        print("ERROR: No path found!") # If we exhaust the queue without finding the destination, throw an error
        return []
    
    def dfs(self, start, destination): # O(V + E) time complexity, O(V) space complexity
        print("-----------------------\nDepth First Search Path\n-----------------------")
        visited = set() # Track visited cities

        def dfs_helper(city, goal, visited, distance): # Inner recursive function
            print(f"{city} (distance: {distance})", end=" ->\n")
            if city == goal: # destination check
                print(f"Total Distance: {distance}")
                return True
            visited.add(city)
            for neighbor, ndistance in self.adjacency_list.get(city, []): # loop through neighbors and recurse
                if neighbor not in visited:
                    if dfs_helper(neighbor, goal, visited, distance + ndistance): 
                        return True
            return False

        result = dfs_helper(start, destination, visited, 0)
        
        if not result: # If we exhaust all paths without finding the destination, throw an error
            print("ERROR: No path found!")
            return []
    
    # heuristic1 will calculate priority by getting the difference between sld of current city and goal city
    def heuristic1(self, city, goal, sld): # O(1) time complexity, O(1) space complexity
        return abs(sld.get(city, 9999) - sld.get(goal, 9999)) # Default to large value (9999) if city not found, otherwise returns priority

    # heuristic2 will calculate priority by triangle inequality between current city and goal city
    def heuristic2(self, city, goal, sld): # O(E) time complexity, O(1) space complexity
        triangle_estimate = sld.get(city, 9999) + sld.get(goal, 9999) # Default to large value (9999) if city not found
        direct_distance = float("inf") # Start with infinity
        for neighbor, dist in self.adjacency_list.get(city, []):
            if neighbor == goal:
                direct_distance = dist
                break
        return min(triangle_estimate, direct_distance) # Return the smaller of the two values as the priority

    def best_first_search(self, start, goal, sld, heuristic): # O(E + V log V) time complexity, O(V) space complexity
        print("----------------------\nBest-First Search Path\n----------------------")
        visited = set() # Track visited cities
        priority_queue = []
        heapq.heappush(priority_queue, (0, start, 0)) # (priority, city, distance)

        while priority_queue:
            _, current, distance = heapq.heappop(priority_queue) # Get city with highest priority (lowest heuristic value)
            if current in visited: # If already visited, skip
                continue
            visited.add(current)
            print(f"{current} (distance: {distance})", end=" ->\n")
            if current == goal: # destination check
                print(f"Total Distance: {distance}")
                return
            for neighbor, ndistance in self.adjacency_list.get(current, []): # loop through neighbors
                if neighbor not in visited:
                    priority = heuristic(neighbor, goal, sld)
                    heapq.heappush(priority_queue, (priority, neighbor, distance + ndistance)) # Add neighbor to priority queue with calculated priority
        
        print("ERROR: No path found!") # If we exhaust the queue without finding the destination, throw an error
        return []
    
    def a_search(self, start, goal, sld, heuristic): # O(E + V log V) time complexity, O(V) space complexity
        print("--------------\nA* Search Path\n--------------")
        priority_queue = []
        heapq.heappush(priority_queue, (0, start, 0)) # (priority, city, distance)
        path = {start: None} # To reconstruct path later if needed
        total_cost = {start: 0} # Cost from start to each city

        while priority_queue:
            _, current, distance = heapq.heappop(priority_queue) # Get city with lowest f(n) = g(n) + h(n)
            print(f"{current} (distance: {distance})", end=" ->\n")
            if current == goal: # destination check
                print(f"Total Distance: {distance}")
                return
            for neighbor, ndistance in self.adjacency_list.get(current, []): # loop through neighbors and calculate cost
                new_cost = total_cost[current] + ndistance
                if neighbor not in total_cost or new_cost < total_cost[neighbor]: # If new cost is lower, update cost and path
                    total_cost[neighbor] = new_cost
                    priority = new_cost + heuristic(neighbor, goal, sld) # Calculate priority using heuristic
                    heapq.heappush(priority_queue, (priority, neighbor, new_cost)) # Add neighbor to priority queue
                    path[neighbor] = current
        
        print("ERROR: No path found!") # If we exhaust the queue without finding the destination, throw an error
        return []

# Straight Line Distance to Bucharest heuristic values
sld_to_bucharest = {
    "Arad": 366, 
    "Bucharest": 0, 
    "Craiova": 160, 
    "Drobeta": 242,
    "Eforie": 161, 
    "Fagaras": 176, 
    "Giurgiu": 77, 
    "Hirsova": 151,
    "Iasi": 226, 
    "Lugoj": 244, 
    "Mehadia": 241, 
    "Neamt": 234,
    "Oradea": 380, 
    "Pitesti": 100, 
    "Rimnicu Vilcea": 193,
    "Sibiu": 253, 
    "Timisoara": 329, 
    "Urziceni": 80, 
    "Vaslui": 199,
    "Zerind": 374, 
    "a": 9999, 
    "b": 9999
}

# Initialize the Romanian roadmap and add roads
romania = RoadMap()
romania.addRoad("Arad", "Zerind", 75)
romania.addRoad("Arad", "Sibiu", 140)
romania.addRoad("Arad", "Timisoara", 118)
romania.addRoad("Bucharest", "Urziceni", 85)
romania.addRoad("Bucharest", "Giurgiu", 90)
romania.addRoad("Bucharest", "Pitesti", 101)
romania.addRoad("Bucharest", "Fagaras", 211)
romania.addRoad("Craiova", "Drobeta", 120)
romania.addRoad("Craiova", "Rimnicu Vilcea", 146)
romania.addRoad("Craiova", "Pitesti", 138)
romania.addRoad("Drobeta", "Mehadia", 75)
romania.addRoad("Eforie", "Hirsova", 86)
romania.addRoad("Fagaras", "Sibiu", 99)
romania.addRoad("Hirsova", "Urziceni", 98)
romania.addRoad("Iasi", "Neamt", 87)
romania.addRoad("Iasi", "Vaslui", 92)
romania.addRoad("Lugoj", "Timisoara", 111)
romania.addRoad("Lugoj", "Mehadia", 70)
romania.addRoad("Oradea", "Zerind", 71)
romania.addRoad("Oradea", "Sibiu", 151)
romania.addRoad("Pitesti", "Rimnicu Vilcea", 97)
romania.addRoad("Rimnicu Vilcea", "Sibiu", 80)
romania.addRoad("Urziceni", "Vaslui", 142)
romania.addRoad("a", "b", 10)  # Test self-loop

romania.printMap()

start_time = time.time()
romania.bfs("Arad", "Bucharest")
print(f"BFS Time: {(time.time() - start_time) * 1000:.3f} ms\n")

start_time = time.time()
romania.dfs("Arad", "Bucharest")
print(f"DFS Time: {(time.time() - start_time) * 1000:.3f} ms\n")

start_time = time.time()
romania.best_first_search("Arad", "Bucharest", sld_to_bucharest, romania.heuristic1)
print(f"Best First Search (heuristic1) Time: {(time.time() - start_time) * 1000:.3f} ms\n")

start_time = time.time()
romania.best_first_search("Arad", "Bucharest", sld_to_bucharest, romania.heuristic2)
print(f"Best First Search (heuristic2) Time: {(time.time() - start_time) * 1000:.3f} ms\n")

start_time = time.time()
romania.a_search("Arad", "Bucharest", sld_to_bucharest, romania.heuristic1)
print(f"A* Search (heuristic1) Time: {(time.time() - start_time) * 1000:.3f} ms\n")

start_time = time.time()
romania.a_search("Arad", "Bucharest", sld_to_bucharest, romania.heuristic2)
print(f"A* Search (heuristic2) Time: {(time.time() - start_time) * 1000:.3f} ms\n")