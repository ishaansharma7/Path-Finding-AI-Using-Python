import adjancy_matrix_gen

def backened(src, obstacles, destination):
    def min_distance(dist, sp_set):                   # choose b/n a vertex from set of vertices connected to parent
        min = 10**10
        global min_index
        for v in range(400):
            if sp_set[v] == False and dist[v]<=min:
                min = dist[v]
                min_index = v
        return min_index

    graph, size = adjancy_matrix_gen.return_matrix()                  # returned adjancy matrix and size
    parent = [-2 for i in range(400)]                   # every element keep track of its parent

    for value in obstacles:                             # gets every obstacle value from list
        for z in range(size):                           # breaks connection of every obstacle with rest in matrix
            graph[z][value]=0

    dist = [10**10 for i in range(size)]                # stores the dist w.r.t to src
    sp_set = [False for i in range(size)]               # tells wheather already selected
    dist[src]=0
    parent[src]=-1

    for i in range(size-1):
        u = min_distance(dist, sp_set)
        sp_set[u]= True
        for v in range(size):
            if sp_set[v] == False and graph[u][v] != 0 and dist[u] != 10**10 and dist[u] + graph[u][v] < dist[v]:
                dist[v] = dist[u] + graph[u][v]
                parent[v] = u

    for i in range(size):
        print(i,'-------',dist[i])
    print(parent)

    def ancestor(dest):
        list1 = []
        stop = dest
        while parent[stop] != -1:               # process of finding ancestory of destination vertex
            print('stop=', stop)
            list1.append(parent[stop])
            stop = parent[stop]
            print('stop=',stop)

        return list1

    destination_parent = ancestor(destination)
    print('parent list',destination_parent)
    return destination_parent
