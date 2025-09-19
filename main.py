import heapq

class RoadMap:
    def __init__(self):
        self.adjacency_list = {}

    def addRoad(self, from_city, to_city, distance):
        if from_city == to_city or [to_city, distance] in self.adjacency_list.get(from_city, []):
            return
        if from_city not in self.adjacency_list:
            self.adjacency_list[from_city] = []
        self.adjacency_list[from_city].append([to_city, distance])
        self.addRoad(to_city, from_city, distance)

    def printMap(self):
        for city, roads in self.adjacency_list.items():
            print(f"{city}: {roads}")

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

romania.printMap()

romania.bfs("Arad", "Sibiu")