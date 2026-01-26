class Graph:
    """
    Undirected graph implementation using an adjacency list.

    Internal representation:
    - self.adj_list is a dictionary
    - key   -> vertex
    - value -> list of adjacent vertices
    """

    def __init__(self):
        """
        Initialize an empty adjacency list.
        No vertices or edges exist at creation.
        """
        self.adj_list = {}

    def print_graph(self):
        """
        Prints each vertex and its adjacency list.

        This method does not modify graph state.
        Time complexity is proportional to total vertices and edges.
        """
        for vertex in self.adj_list:
            # Each vertex is printed along with its list of neighbors
            print(vertex, " : ", self.adj_list[vertex])

    def add_vertex(self, vertex):
        """
        Adds a new vertex to the graph.

        Logic:
        1. Check if the vertex already exists.
        2. If not present, create an empty adjacency list for it.
        3. Return True if insertion happens, otherwise False.
        """

        # Vertex must be unique; dictionary keys enforce uniqueness
        if vertex not in self.adj_list:
            # Initialize adjacency list for the new vertex
            self.adj_list[vertex] = []
            return True

        # Vertex already exists; no changes made
        return False

    def add_edge(self, v1, v2):
        """
        Adds an undirected edge between v1 and v2.

        Logic:
        1. Verify that both vertices exist.
        2. Append v2 to v1's adjacency list.
        3. Append v1 to v2's adjacency list.
        4. Return True if edge is added.
        """

        # Both vertices must exist before an edge can be formed
        if v1 in self.adj_list and v2 in self.adj_list:

            # Add v2 as a neighbor of v1
            self.adj_list[v1].append(v2)

            # Add v1 as a neighbor of v2 (undirected graph)
            self.adj_list[v2].append(v1)

            return True

        # Edge cannot be created if either vertex is missing
        return False

    def remove_edge(self, v1, v2):
        """
        Removes an undirected edge between v1 and v2.

        Logic:
        1. Ensure both vertices exist.
        2. Attempt to remove v2 from v1's adjacency list.
        3. Attempt to remove v1 from v2's adjacency list.
        4. Ignore failure if the edge does not exist.
        """

        # Removal only makes sense if both vertices exist
        if v1 in self.adj_list and v2 in self.adj_list:
            try:
                # Remove v2 from v1's adjacency list
                self.adj_list[v1].remove(v2)

                # Remove v1 from v2's adjacency list
                self.adj_list[v2].remove(v1)

            except ValueError:
                # ValueError occurs if the edge does not exist
                # Graph remains unchanged in this case
                pass

            return True

        # One or both vertices do not exist
        return False

    def remove_vertex(self, vertex):
        """
        Removes a vertex and all edges connected to it.

        Logic:
        1. Verify vertex exists.
        2. Iterate through all its neighbors.
        3. Remove the vertex from each neighbor's adjacency list.
        4. Delete the vertex from the graph.
        """

        # Vertex must exist to be removed
        if vertex in self.adj_list:

            # Iterate through all vertices connected to this vertex
            for neighbor in self.adj_list[vertex]:
                # Remove the vertex from each neighbor's adjacency list
                self.adj_list[neighbor].remove(vertex)

            # Finally remove the vertex itself
            del self.adj_list[vertex]

            return True

        # Vertex does not exist
        return False


# ---------------------------
# Example Usage 
# ---------------------------

# Step 1: Create an empty graph
my_graph = Graph()

# Step 2: Add vertices to the graph
my_graph.add_vertex('A')
my_graph.add_vertex('B')
my_graph.add_vertex('C')
my_graph.add_vertex('D')

# Step 3: Verify vertex-only state (no edges yet)
my_graph.print_graph()

# Step 4: Add undirected edges
my_graph.add_edge('A', 'B')
my_graph.add_edge('A', 'C')
my_graph.add_edge('A', 'D')
my_graph.add_edge('B', 'D')
my_graph.add_edge('C', 'D')

# Step 5: Verify adjacency lists after edge creation
my_graph.print_graph()

# Step 6: Remove a high-degree vertex
my_graph.remove_vertex('D')

# Step 7: Verify graph consistency after vertex removal
my_graph.print_graph()