"""
    Implement the Depth-First Search Algorithm

Implement the Depth-First Search Algorithm

In this lab, you will implement a graph traversal algorithm called depth-first search.

Whereas the breadth-first search searches incremental edge lengths away from the source node, 

depth-first search first goes down a path of edges as far as it can.

Once it reaches one end of a path, the search will backtrack to the last node with an un-visited 

edge path and continue searching.

Unlike breadth-first search, every time a node is visited, it doesn't visit all of its neighborhood. 

Instead, it first visits one of its neighborhood and continues down that path until there are no more 

nodes to be visited on that path.

To implement this algorithm, you'll want to use a stack (an array where the last element 

added is the first to be removed, following the Last-In-First-Out principle). 

A stack is helpful in depth-first search algorithms because, as you add neighborhood to the stack, 

you want to visit the most recently added neighborhood first and remove them from the stack.

A simple output of this algorithm is a list of nodes which are reachable from a given node.

Therefore, you'll also want to keep track of the nodes you visit.

Objective: Fulfill the user stories below and get all the tests to pass to complete the lab.

User Stories:

    You should have a function named dfs.
    The dfs function should take two arguments:
        An undirected, adjacency matrix.
        A node label, which is the numeric value of the node between 0 and n - 1, where n is the total number of nodes in the graph.
    The dfs function should implement the depth-first search algorithm to output a list of all nodes reachable from the node passed to it.

Tests:

    Waiting: 1. You should have a function named dfs that takes two arguments.
    Waiting: 2. dfs([[0, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0]], 1) should return a list with 1, 2, 3, and 0.
    Waiting: 3. dfs([[0, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0]], 3) should return a list with 1, 2, 3, and 0.
    Waiting: 4. dfs([[0, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 0]], 3) should return [3].
    Waiting: 5. dfs([[0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]], 3) should return a list with 3 and 2.
    Waiting: 6. dfs([[0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]], 0) should return a list with 0 and 1.
    Waiting: 7. The dfs function should return the correct results.

"""

def dfs(adjMatrx: list, start_node: int) -> list:
    """
    Function qui retourne une liste de tous les noeuds atteignables depuis
    le noeud spécifié
    """
    # Nombre de noeuds
    n = len(adjMatrx)

    if start_node >= n:
        raise ValueError("start_node est hors de la Matrix")
    # liste des noeuds atteignables partant de start_node
    result = []
    
    # Stack de tous les voisins récemment visités
    neighborhood = [start_node ]

    # Liste déterminant les noeuds déjà visités
    visited = [False]* n 

    while neighborhood:
        # Noeud à explorer
        current_node = neighborhood.pop()
    
        if not visited[current_node]:
            result.append(current_node)
            visited[current_node] = True
            for neighbor in range(n):
                if adjMatrx[current_node][neighbor] != 0 and not visited[neighbor]:
                    neighborhood.append(neighbor)
                    
    return result 


#print(dfs([[0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]], 0))
print(dfs([[0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]], 3))
#print(dfs([[0, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 0]], 3))
#print( dfs([[0, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0]], 3))
#print(dfs([[0, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0]], 1))