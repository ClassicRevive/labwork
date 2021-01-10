def make_edge_list(adjacency):
    """ this function create an edge list representation of a graph using the supplied adjacency matrix
    """
    # assuming cardinality <= 26
    edge_names = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # Maybe start with an empty edge_list
    edge_list = []
    
    for row in adjacency:  # parse each row of matrix
        tmp = []
        for i in range(len(row)):  # within each row find 1s and add corresponding edge to list
            if row[i] == 1:
                tmp.append(edge_names[i])
        
        edge_list.append(tmp)  # add this row to edge list



    return edge_list


def make_adjacency_matrix(edge_list):
    """ this function create an adjacency matrix representation of a graph using the supplied edge list
    """
    # Maybe start with an empty adjacency matrix
    adjacency_matrix = []

    # assuming cardinality <= 26
    edge_names = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    row_length = len(edge_list)
    edges = edge_names[:row_length]
    
    for lst in edge_list:  # parse each sublist
        tmp = []
        for i in range(row_length):
            if edges[i] in lst:  # if edges[i] is in edge list, add 1
                tmp.append(1)
            else:  # otherwise add 0
                tmp.append(0)

        adjacency_matrix.append(tmp)  # add this row to edge list

    
    return adjacency_matrix


def make_adjacency_matrix2(edge_list):
    ''' this is a second version of the above function '''

    adjacency_matrix = []
    num_nodes = len(edge_list)

    for i in range(num_nodes):
        adjacency_matrix.append([0 for i in range(num_nodes)])


    for row in range(len(adjacency_matrix)):
        for col in range(num_nodes):
            for j in edge_list[row]:
                if ord(j) - ord('A') == col:
                    adjacency_matrix[row][col] = 1

    return adjacency_matrix

