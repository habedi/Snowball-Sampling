import networkx as nx
import Queue as que
import copy
from numpy.random import randint

def randomseed(g):
    ux = randint(0,g.number_of_nodes(),1)
    return ux[0]

def snowballsampling(g, seed, maxsize=50):
    if g.number_of_nodes() < maxsize:
        return [None]
    q = que.Queue()
    q.put(seed)
    subgraph = [seed]
    while not q.empty():
        for node in g.neighbors(q.get()):
            if len(set(subgraph)) < maxsize:
                q.put(node)
                subgraph.append(node)
            else :
                return list(set(subgraph))
            pass
        pass
    return list(set(subgraph))

def surroundings(g, subgraph):
    surdngs = copy.copy(subgraph)
    for node in subgraph:
        for i in g.neighbors(node):
            if i not in surdngs:
                surdngs.append(i)
                pass
            pass
        pass
    return surdngs


    
