import time
from reachability import *
from collections import defaultdict
from reader import *
import sys
import random
import numpy as np

options = {
        'chicagoRegional': readChicagoRegional,
        'moreno_blogs': readMoreno,
        'moreno_highschool': readMorenoHighSchool,
        'soc-Epinions1.txt': readEpinion,
        'usairport': readUSAirport,
        'airtraffic': readAirTraffic,
        'test': readTest
}

if __name__ == '__main__':
    folder = 'datasets'
    filename = sys.argv[1]
    N, records = options[filename](folder, filename)

    L = defaultdict(set)
    for (node1, node2) in records:
        L[node1].add(node2)
    print("Building the maximum 2-hop labeling.")
    start = time.time()
    maxL = maximumLabelingL(L, N)
    end = time.time()
    print(end - start, ' seconds.')

    start = time.time()
    S = defaultdict(set)
    S_in = defaultdict(set)
    S_out = defaultdict(set)
    isolated = set()
    InGoing = defaultdict(set)
    OutGoing = defaultdict(set)
    InNodes = set()
    OutNodes = set()

    #sample_size = 20
    #random_nodes = random.choices([i for i in range(N)], k=sample_size)
    #for u in random_nodes:
    for u in range(N):
        for v in range(N):
            if u == v:
                continue
            #connected_nodes = (maxL[u]['out'] | {u}) & (maxL[v]['in'] | {v})
            connected_nodes = maxL[u]['out'] & maxL[v]['in']
            if not connected_nodes:
                if (maxL[u]['out'] | {u}) & (maxL[v]['in'] | {v}):
                    isolated.add((u, v))
                continue
            #print(u, v, connected_nodes)
            InNodes.add(v)
            OutNodes.add(u)

            for cn in connected_nodes:
                S_in[cn].add(u)
                S_out[cn].add(v)
                S[cn].add((u, v))
                InGoing[v].add((u, v))
                OutGoing[u].add((u, v))

        #print(u)
    print('Building S takes %f seconds.' %(time.time() - start))
    #print('S:', S)
    T = set()
    for u in range(N):
    #for u in random_nodes:
        for v in range(N):
            if u == v:
                continue

            #if (maxL[u]['out'] | {u}) & (maxL[v]['in'] | {v}):
            if maxL[u]['out'] & maxL[v]['in']:
                T.add((u, v))

    OptL = [defaultdict(set) for _ in range(N)]
    #print('T:', T)
    #print('InGoing', InGoing)
    #print('OutGoing', OutGoing)
    #print('InNodes', InNodes)
    #print('OutNodes', OutNodes)
    workingT = T.copy()

    while len(workingT) > 0:
        maxScore = -1
        target = -1
        for u in range(N):
            #print("Node %d:" %u)
            #print(u, S[u], S_in[u], S_out[u])
            if not S[u]:
                continue

            if not (S_in[u] & OutNodes) | (S_out[u] & InNodes):
                continue
            score = len(set(S[u]) & workingT) / (len(S_in[u] & OutNodes) + len(S_out[u] & InNodes))
            #print('Score: %f' %score)
            if score > maxScore:
                maxScore = score
                target = u
        #print()
        #print('Update 2-hop labeling')
        if target != -1:
            #print('select %d.' %target)
            for (lout, lin) in S[target].copy():
                #print(lout, lin)
                OptL[lout]['out'].add(target)
                OptL[lin]['in'].add(target)
                workingT.remove((lout, lin))
                OutGoing[lout].remove((lout, lin))
                InGoing[lin].remove((lout, lin))

                for key, values in S.items():
                    if (lout, lin) in values:
                        values.remove((lout, lin))

                if len(OutGoing[lout]) == 0:
                    OutNodes.remove(lout)

                if len(InGoing[lin]) == 0:
                    InNodes.remove(lin)

    #process isolated edges
    for (u, v) in isolated:
        if (OptL[u]['out'] | {u}) & (OptL[v]['in'] | {v}):
           continue
        else:
            OptL[u]['out'].add(v)
    '''
    print("maxL:")
    for i in range(1, N):
        print(i, maxL[i])
    print("OptL:")
    for i in range(1, N):
        print(i, OptL[i])
    '''
    print('Checking errors. if no print info about errors just below, the optimized 2-hop labeling is correct.')
    for u in range(N):
        for v in range(N):
            if u == v:
                continue
            if (maxL[u]['out'] | {u}) & (maxL[v]['in'] | {v}):
                if not (OptL[u]['out'] | {u}) & (OptL[v]['in'] | {v}):
                    print('error:', u, v)

    maxSize = 0
    optSize = 0
    for i in range(1, N):
        maxSize += len(maxL[i]['out'])
        maxSize += len(maxL[i]['in'])
        optSize += len(OptL[i]['out'])
        optSize += len(OptL[i]['in'])

    print('maxSize: %d; optSize: %d.' % (maxSize, optSize))





