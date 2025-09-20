import heapq

class RoadMap:
    def __init__(self):
        self.adjacency_list = {}

    def addRoad(self, from_city, to_city, distance):
        if from_city == to_city:
            return
        if (to_city, distance) in self.adjacency_list.get(from_city, []):
            return
        if from_city not in self.adjacency_list:
            self.adjacency_list[from_city] = []
        self.adjacency_list[from_city].append((to_city, distance))
        self.addRoad(to_city, from_city, distance)

    def printMap(self):
        for city, roads in self.adjacency_list.items():
            print(f"{city}: {roads}")

    def bfs(self, start, destination):
        print("-------------------------\nBreadth First Search Path\n-------------------------")
        visited = set()
        queue = [(start, 0)]

        while queue:
            current, distance = queue.pop(0)
            print(f"{current} (distance: {distance})", end=" ->\n") 
            if current == destination:
                print(f"Total Distance: {distance}")
                return
            if current not in visited:
                visited.add(current)
                for neighbor, ndistance in self.adjacency_list[current]:
                    if neighbor not in visited:
                        queue.append((neighbor, distance + ndistance))
    
    def dfs(self, start, destination):
        print("-----------------------\nDepth First Search Path\n-----------------------")
        visited = set()

        def dfs_helper(city, goal, visited, distance):
            print(f"{city} (distance: {distance})", end=" ->\n")
            if city == goal:
                print(f"Total Distance: {distance}")
                return True
            visited.add(city)
            for neighbor, ndistance in self.adjacency_list.get(city, []):
                if neighbor not in visited:
                    if dfs_helper(neighbor, goal, visited, distance + ndistance):
                        return True
            return False

        dfs_helper(start, destination, visited, 0)



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

romania.bfs("Arad", "Bucharest")
romania.dfs("Arad", "Bucharest")
romania.best_search("Arad", "Bucharest")