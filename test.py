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
    print("build max Labeling takes ", end - start, ' seconds.')

    count = 0
    trials = 40
    T = 0
    for i in range(N):
        maxNum = max(trials, len(L[i]))
        if maxNum <= trials:
            for j in L[i]:
                count += 1
                start = time.time()
                deleteL(L, maxL, N, i, j)
                T += (time.time() - start)
                L[i].add(j)
                if count % 100 == 0:
                    print(count, T / count)
        else:
            candidates = set()
            for c in L[i]:
                candidates.add(c)
            for _ in range(trials):
                t_index = random.randint(0, len(candidates) - 1)
                candidates_list = list(candidates)
                t = candidates_list[t_index]
                candidates.remove(t)
                count += 1
                start = time.time()
                deleteL(L, maxL, N, i, t)
                T += (time.time() - start)
                L[i].add(t)
                if count % 100 == 0:
                    print(count, T / count)

    print(count, T / count)
