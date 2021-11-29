import sys


# Function to find the minimum distance from the list dist that is storing the minimum distance to that edge
# this function takes three arguments
# 1- list of dist storing minimum distance
# 2- list storing which node has been processed so far not
# 3- total nodes in the graph
def getMinNode(dist, processed, nodes):
    # storing the maximum value to save the minimum distance from dist list
    minimum = sys.maxsize
    # for storing the node with minimum distance/cost/weight
    minNode = -1

    # iterating through the total nodes in the graph
    for a in range(0, nodes):
        # checking if the node is not processed and distance is minimum
        if not processed[a] and dist[a] < minimum:
            # storing the minimum node
            minNode = a
            # storing the minimum distance
            minimum = dist[a]

    return minNode


# Algorithm takes the graph encoded a matrix
# Each row of the graph represents the corresponding row no as the node
# with the edges along with their weights
# It only works with the undirected graphs encoded in a matrix
# This functions takes three arguments
# 1- Graph, 2- size of the graph (no of rows/cols both are same because graph is encoded in a matrix),
# 3- started node for the Minimum Spanning Tree
def prims(graph, totalNodes, startingNode):
    # List to store the parent and child
    # Index of the list represents the parent, the value stored in the corresponding index stores the child
    mst = []

    # List to store the nodes that have already been processed and connected to the nearest edge with the least cost
    processed = []

    # List to stores the distance of parent with the child
    # The index represents the parent and the distance is stored at that index for whatever child the
    # algorithm is processing for that parent at the moment
    dist = []

    # Iterates to the total no of nodes in the graph to initialize the three lists above
    for a in range(0, totalNodes):
        # Stores the maximum distance for every node in the list
        dist.append(sys.maxsize)
        # Declares that no node has been processed so far
        processed.append(False)
        # Stores no edge has been assigned to any node at the moment
        mst.append(-1)

    # Sets the distance to starting node as 0 so that it is chosen first
    # In this way, the starting node becomes the root of the Minimum Spanning Tree (MST)
    dist[startingNode] = 0

    # Runs the loop for nodes - 1
    for a in range(0, totalNodes - 1):
        # finds the edge with the minimum cost/weight in the graph
        minNode = getMinNode(dist, processed, totalNodes)

        # mark that node as processed
        processed[minNode] = True

        # runs the loop again for all the nodes in the graph to find the corresponding edges having minimum distance
        for b in range(0, totalNodes):
            # Checks if there is an edge with a valid weight (0 shows that the edge doesn't exist) and
            # if the node has not been processed yet and
            # distance/cost/weight from the node to the minimum distance edge found above is minimum than already saved
            # distance/cost/weight in any other iterations happened before
            if graph[minNode][b] != 0 and not processed[b] and graph[minNode][b] < dist[b]:
                # when the condition is true
                # saves the newly found minimum distance in the distance list for the corresponding node
                dist[b] = graph[minNode][b]
                # stores the minimum distance node just found which is to be the edge of the node b
                mst[b] = minNode

    # iterates till the total nodes in the graph to display the parent node, child node, and the corresponding weight
    for a in range(0, totalNodes):
        # a condition to determine that there is valid edge to the node and
        if mst[a] != -1:
            print(mst[a], "-->", a, ": ", graph[a][mst[a]])


if __name__ == '__main__':
    # The graph with 8 nodes 0 - 8
    _graph = [[0, 1, 0, 0, 0, 0, 0, 0],
              [1, 0, 28, 0, 0, 0, 10, 0],
              [0, 28, 0, 16, 0, 0, 0, 14],
              [0, 0, 16, 0, 12, 0, 0, 0],
              [0, 0, 0, 12, 0, 22, 0, 18],
              [0, 0, 0, 0, 22, 0, 25, 24],
              [0, 10, 0, 0, 0, 25, 0, 0],
              [0, 0, 14, 0, 18, 24, 0, 0]]

    # Calling the Prims Algorithm
    # It takes the graph as a first argument
    # It takes the size of the graph as second argument
    # It takes the starting node as third argument
    prims(_graph, 8, 6)
