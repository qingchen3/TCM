import time
from reachability import *
from collections import defaultdict
from reader import *
import random
import numpy as np
import sys

options = {
        'chicagoRegional': readChicagoRegional,
        'moreno_blogs': readMoreno,
        'soc-Epinions1.txt': readEpinion,
        'usairport': readUSAirport,
        'airtraffic': readAirTraffic
        }


if __name__ == '__main__':
    folder = 'datasets'
    filename = sys.argv[1]
    N, records = options[filename](folder, filename)

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
    #ratio_list = [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1, 0.2, 0.3, 0.4, 0.5]
    ratio_list = [0.05]
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
            #print("%d, size of Lin: %d, size of Lout: %d." %(i, len(maxL[i]['in']), len(maxL[i]['out'])))

            total_out += len(maxL[i]['out'])
            total_in += len(maxL[i]['in'])
            sample_out += len(RL[i]['out'])
            sample_in += len(RL[i]['in'])
        print("ratio: %f" % ratio)
        print("total size of Lin: %d, total size of Lout: %d, sum of sample size of Lin: %d, sum of sample size of Lout: %d." % (total_out, total_in, sample_in, sample_out))
        count = 0
        hit = 0

        for u in range(N):
            for v in range(N):
                if len(maxL[u]['out'] & maxL[v]['in']) == 0:
                    continue
                if u == v:
                    continue

                count += 1
                if len(RL[u]['out'] & RL[v]['in']) > 0:
                    hit += 1

        print('hit: %d, count: %d' % (hit, count))
        print('precission: %f' % (hit / count))

        print('Inserting edges.')
        number_list = [i for i in range(N)]
        tn = 10
        threshold = 2
        for u in range(N):
            random_list = random.choices(number_list, k = tn * 4)
            print(u, random_list)
            tcount = 0
            for r in random_list:
                if tcount == tn or u == r or r in RL[u]['out'] or u in RL[r]['in']:
                    continue
                tcount += 1
                print('Inserting %d->%d' %(u, r))
                insertL(L, RL, u, r)
                insertL(L, maxL, u, r)

                print("size of L_out of node %d: %d, size of L_in of node %d: %d" %(u, len(RL[u]['out']),  r, len(RL[r]['in'])))
                if len(RL[u]['out']) > threshold * size:
                    RL[u]['out'] = set(random.choices(list(RL[u]['out']), k = size))

                    print("resampling on L_out of node %d" % u)
                    print("After resampling, size of L_out of node %d: %d, size of L_in of node %d: %d" % (
                    u, len(RL[u]['out']), r, len(RL[r]['in'])))
                    count = 0
                    hit = 0
                    for tv in range(N):
                        if len(maxL[u]['out'] & maxL[tv]['in']) == 0:
                            continue
                        if u == tv:
                            continue

                        count += 1
                        if len(RL[u]['out'] & RL[tv]['in']) > 0:
                            hit += 1

                    print('After resampling: hit: %d, count: %d' % (hit, count))
                    print('After resampling: precission: %f' % (hit / count))
                    print()

                if len(RL[r]['in']) > threshold * size:
                    RL[r]['in'] = set(random.choices(list(RL[r]['in']), k = size))

                    print("resampling on L_in of node %d" % r)
                    print("After resampling, size of L_out of node %d: %d, size of L_in of node %d: %d" % (
                    u, len(RL[u]['out']), r, len(RL[r]['in'])))
                    count = 0
                    hit = 0
                    for tu in range(N):
                        if len(maxL[tu]['out'] & maxL[r]['in']) == 0:
                            continue
                        if tu == r:
                            continue

                        count += 1
                        if len(RL[tu]['out'] & RL[r]['in']) > 0:
                            hit += 1

                    print('After resampling: hit: %d, count: %d' % (hit, count))
                    print('After resampling: precission: %f' % (hit / count))
                    print()

                if len(RL[r]['in']) <= threshold * size and len(RL[u]['out']) <= threshold * size:
                    print('No resampling')
                    print(" size of L_out of node %d: %d, size of L_in of node %d: %d" % (
                    u, len(RL[u]['out']), r, len(RL[r]['in'])))
                    count = 0
                    hit = 0

                    for ou in maxL[u]['out']:
                        for ir in maxL[r]['in']:
                            if len(maxL[ou]['out'] & maxL[ir]['in']) == 0:
                                continue
                            if ou == ir:
                                continue

                            count += 1
                            if len(RL[ou]['out'] & RL[ir]['in']) > 0:
                                hit += 1

                    print('No resampling: hit: %d, count: %d' % (hit, count))
                    if hit == 0:
                        print('hit == 0')
                    else:
                        print('No resampling: precission: %f' % (hit / count))
                    print()

                print()
