from collections import deque

#Обход графа
graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

# graph["you"] = ["egor", "pomidor"]
# graph["egor"] = []
# graph["pomidor"] = []

# print(graph[graph["you"][0]])
search_deque = deque()
search_deque += graph["you"]
searched = []
flag = True
while (search_deque) and flag:     #пока очередь не пустая
    person = search_deque.popleft()    #из очереди извлекается 1 человек
    if not person in searched:
        print(person) 
        if person == "thom":
            print(f"Niceee, this is {person}")
            flag = False
        else:
            search_deque += graph[person]
            searched.append(person)
print(searched)


#Алгоритм Дейкстры
#Таблица для хранения графа
graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["fin"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

graph["fin"] = {}


#Таблица стоимости
inf = float("inf")
costs = {}
costs["a"] = graph["start"]["a"]
costs["b"] = graph["start"]["b"]
costs["fin"] = inf

#Родители наших точек
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

proccesed = []

def find_lowed_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in proccesed:
            lowest_cost = cost 
            lowest_cost_node = node
    return lowest_cost_node

node = find_lowed_cost_node(costs) #Найти узел с наименьшей стоимостью'
#node - узел (a или b)
while node != None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    proccesed.append(node)
    node = find_lowed_cost_node(costs)
print(costs["fin"])





