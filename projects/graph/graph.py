"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()
        

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist!")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id     ]

    def bft(self, starting_vertex):
        # Create a queue to hold nodes to visit
        to_visit = Queue()

        # Create a set to hold visited nodes
        visited = set()

        # Initalize: add the starting node to the queue
        to_visit.enqueue(starting_vertex)

        # While queue not empty:
        while to_visit.size() > 0:
            # dequeue first entry
            v = to_visit.dequeue()

            # if not visited:
            if v not in visited:
                # Visit the node (print it out)
                print(v)

                # Add it to the visited set
                visited.add(v)

                # enqueue all its neighbors
                for n in self.get_neighbors(v):
                    #print(f"Adding: {n}")
                    to_visit.enqueue(n)
        
        

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create a queue to hold nodes to visit
        to_visit = Stack()

        # Create a set to hold visited nodes
        visited = set()

        # Initalize: add the starting node to the queue
        to_visit.push(starting_vertex)

        # While queue not empty:
        while to_visit.size() > 0:
            # pop first entry
            v = to_visit.pop()

            # if not visited:
            if v not in visited:
                # Visit the node (print it out)
                print(v)

                # Add it to the visited set
                visited.add(v)

                # push all its neighbors
                for n in self.get_neighbors(v):
                    #print(f"Adding: {n}")
                    to_visit.push(n)

    def dft_recursive(self, starting_vertex, visited = set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # Add current node to visited
        visited.add(starting_vertex)
        # Print current node
        print(starting_vertex)
        # Save all current node neighbors to a variable
        neighbors = self.get_neighbors(starting_vertex)
        # While the current node has neighbors
        while len(neighbors) > 0:
            # For each neighnbor
            for each in neighbors:
                # If it has not been visited already
                if each not in visited:
                    # Rerun the function, replacing the current node with the neighbor
                    self.dft_recursive(each, visited)
                # If it has been visited
                else:
                    return

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty queue and enqueue A PATH TO the starting vertex ID
        to_visit = Queue()
        to_visit.enqueue([starting_vertex])

        # Create a Set to store visited vertices
        visited = set()

        # While the queue is not empty...
        while to_visit.size() > 0:
            # Dequeue the first PATH
            path = to_visit.dequeue()
            # Grab the last vertex from the PATH
            v = path[-1]
            # If that vertex has not been visited...
            if v not in visited:
                # CHECK IF IT'S THE TARGET
                if v == destination_vertex:
                # IF SO, RETURN PATH
                    return path
                # Mark it as visited...
                visited.add(v)
                # Then add A PATH TO its neighbors to the back of the queue
                for i in self.get_neighbors(v):               
                    # COPY THE PATH
                    path_copy = path.copy() 
                    # APPEND THE NEIGHOR TO THE BACK
                    path_copy.append(i)
                    to_visit.enqueue(path_copy)

        

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create empty stack
        s = Stack()
        # Push the starting node
        s.push([starting_vertex])
        # Create a set for visited vertices
        visited = set()
        # While stack is not empty
        while s.size() > 0:
            # Create current path variable set to first node in s
            currentPath = s.pop()
            # Set the last node in the currentPath to a variable
            lastNode = currentPath[-1]
            # If it hasnt been visited
            if lastNode not in visited:
                # Check if it is the destination
                if lastNode == destination_vertex:
                    # Return the path if it is
                    return currentPath
                # If it is not the target
                else:
                    # Add the lastNode to visited
                    visited.add(lastNode)
                    # Set the lastNode neighbors to variable
                    neighbors = self.get_neighbors(lastNode)
                    # For each of lastNodes neighbors
                    for neighbor in neighbors:
                        # Copy the path current path
                        copy = currentPath[:]
                        # Add the neighbor
                        copy.append(neighbor)
                        # Add the copy to the s
                        s.push(copy)

    def dfs_recursive(self, starting_vertex, destination_vertex, path=Stack(), visited=set()):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        This should be done using recursion.
        """
        # Create a path, this will be None the first time this function runs
        currentPath = path.pop()
        # If currentPath is None
        if currentPath == None:
            # Make currentPath the starting vertex
            currentPath = [starting_vertex]
        # Check if the last node in the currentPath is not in visited
        if currentPath[-1] not in visited:
            # Add the last node to visited
            visited.add(currentPath[-1])
            # For each of the last nodes neighbors
            for neighbor in self.get_neighbors(currentPath[-1]):
                # If the neighbor is the destination
                if neighbor == destination_vertex:
                    # Append that neighbor to the currentPath
                    currentPath.append(neighbor)
                    # Return the currentPath
                    return currentPath
                # Create a copy of the currentPath
                copy = currentPath.copy()
                # Add the neighbor to the copy
                copy.append(neighbor)
                # Push the copy to the reoccuring path
                path.push(copy)
            # Rerun the function with updated values
            return self.dfs_recursive(starting_vertex, destination_vertex, path, visited)


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
