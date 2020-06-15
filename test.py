import time
from reachability import *
from collections import defaultdict
from reader import *
import random
import numpy as np

if __name__ == '__main__':
    folder = 'datasets'
    filename = 'moreno_blogs'
    N, records = readMoreno(folder, filename)
    #M = np.zeros([N, N], dtype = int)
    L = defaultdict(set)
    for (node1, node2) in records:
        # nodes = line.rstrip().split('\t')
        #M[node1][node2] = 1
        L[node1].add(node2)
    print("Building the maximum 2-hop labeling.")
    start = time.time()
    #bfsl(L, N, 1)
    maxL = maximumLabelingL(L, N)
    end = time.time()
    print(end - start, ' seconds.')
    sum_in = 0
    sum_out = 0
    RL = [defaultdict(set) for _ in range(N)]
    ratio_list = [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09]
    for ratio in ratio_list:
        size = int(ratio * N)
        total_out = 0
        total_in = 0
        sample_out = 0
        sample_in = 0
        for i in range(len(maxL)):
            if len(maxL[i]['in']) > size:
                RL[i]['in'] = set(random.choices(list(maxL[i]['in']), k = size))
            else:
                RL[i]['in'] = maxL[i]['in'].copy()

            if len(maxL[i]['out']) > size:
                RL[i]['out'] = set(random.choices(list(maxL[i]['out']), k = size))
            else:
                RL[i]['out'] = maxL[i]['out'].copy()

            total_out += len(maxL[i]['out'])
            total_in += len(maxL[i]['in'])
            sample_out += len(RL[i]['out'])
            sample_in += len(RL[i]['in'])
        print("ratio: %f" % ratio)
        print(
            "total size of Lin: %d, total size of Lout: %d, sum of sample size of Lin: %d, sum of sample size of Lout: %d." % (
            total_out, total_in, sample_in, sample_out))
        count = 0
        hit = 0

        for u in range(N):
            for v in range(N):
                if len(maxL[u]['out'] & maxL[v]['in']) == 0:
                    continue
                count += 1
                if len(RL[u]['out'] & RL[v]['in']) > 0:
                    hit += 1

        print('hit: %d, count: %d' % (hit, count))
        print('precission: %f' % (hit / count))
        print()
