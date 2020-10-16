
def detectCycle(g,v,visited,parents,parent):
    visited[v] = True
    parents[v ] = parent
    
    for each in g[v]:
        if visited[each] is False:
            if detectCycle(g,each,visited,parents,v):
                return True
        elif parent!= each:
            return True
    return False
    
    
def isCyclic(g,n):
    '''
    :param g: given adjacency list representation of graph
    :param n: no of nodes in graph
    :return:  boolean (whether a cycle exits or not)
    '''
    # code here
    visited = [False]*n
    # parents = [-1]*n
    parents = [-1]*n
    for each in g:
        if visited[each] is False:
            if detectCycle(g,each,visited,parents,-1):
                return 1
    return 0