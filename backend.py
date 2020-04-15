import adjancy_matrix_gen
import copy


def backened(src, obstacles, destination):
    def min_distance(dist, sp_set):                   # choose b/n a vertex from set of vertices connected to parent
        min = 10**10
        global min_index
        for v in range(400):                        # minimum distant adjacent vertex is chosen
            if sp_set[v] == False and dist[v]<=min:
                min = dist[v]
                min_index = v
        return min_index

    graph, size = copy.deepcopy(adjancy_matrix_gen.return_matrix())    # returns adjacency matrix and size
    parent = [-2 for i in range(400)]                   # every vertex keep track of its parent vertex

    for value in obstacles:                             # gets every obstacle value from list
        for z in range(size):                           # breaks connection of every obstacle with rest in matrix
            graph[z][value] = 0

    dist = [10**10 for i in range(size)]                # stores the dist w.r.t to src
    sp_set = [False for i in range(size)]               # tells whether already selected or covered along path
    dist[src] = 0
    parent[src] = -1

    for i in range(size-1):
        u = min_distance(dist, sp_set)                  # returns the minimum distant adjacent vertex
        sp_set[u] = True
                                         # find all the vertices connected to the selected vertex u
        for v in range(size):
            if sp_set[v] is False and graph[u][v] != 0 and dist[u] != 10**10 and dist[u] + graph[u][v] < dist[v]:
                dist[v] = dist[u] + graph[u][v]
                parent[v] = u

    # for i in range(size):
    #     print(i, '-------', dist[i])
    # print(parent)

    def ancestor(dest):
        list1 = []
        stop = dest
        while parent[stop] != -1:               # process of finding ancestory of destination vertex
            list1.append(parent[stop])
            stop = parent[stop]

        return list1

    destination_parent = ancestor(destination)
    #print('parent list', destination_parent)
    return destination_parent
