import os
import numpy as np
import time
from reachability import *
from collections import defaultdict
from reader import *
import random

if __name__ == '__main__':
    folder = 'datasets'

    # filename = 'soc-Epinions1.txt'
    # filename = 'moreno_blogs'
    filename = 'moreno_blogs'

    # reader = open(os.path.join(folder, filename), 'r')

    # N = 76000
    N, records = readMoreno(folder, filename)
    L = defaultdict(set)
    #M = np.zeros([N, N], dtype=int)
    for (node1, node2) in records:
        # nodes = line.rstrip().split('\t')
        # M[int(nodes[0])][int(nodes[1])] = 1
        L[node1].add(node2)

    print("finishing building adjacency list.")
    start = time.time()
    # maxL = maximumLabelingM(M)
    maxL = maximumLabelingL(L, N)
    # res = BFSL(L, N, 1)
    end = time.time()
    print("building maximum labeling takes ", end - start, ' seconds.')

    count = 0
    trials = 10
    T = 0
    for i in range(N):
        t = 0
        neighbors = L[i].copy()
        while t < trials:
            j = random.randint(0, N)
            if j not in neighbors and j in L:
                t += 1
                count += 1
                start = time.time()
                insertL(L, maxL, i, j)
                T += (time.time() - start)
                neighbors.add(j)
                #deleteL(L, maxL, N, i, j)
                if count % 100 == 0:
                    print(count, T / count)


