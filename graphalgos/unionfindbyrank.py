parent = [node for node in range(n)]
rank = [1]*n

def find(node):
    while node != parent[node]:
        parent[node] = parent[parent[node]]
        # the cool comprehension
        node = parent[node]
    return node

def union(node1, node2):
    parent1, parent2 = find(node1), find(node2)

    if parent1 == parent2:
        return [node1, node2]

    node1, node2 = parent1, parent2
    if rank[node1] > rank[node2]:
        parent[node2] = node1

    elif rank[node1] < rank[node2]:
        parent[node1] = node2

    else:
        parent[node2] = node1
        rank[node1] += 1

    return []
