import queue
from collections import defaultdict

def reachable(L, u, v):
    visited = [0 for _ in range(N)]
    q = queue.Queue()
    visited[u] = 1
    q.put(u)
    while q.qsize() > 0:
        node = q.get()
        if node == v:
            return True
        for neighbor in L[node]:
            if visited[neighbor] != 1:
                q.put(neighbor)
                visited[neighbor] = 1

    return False

def bfsm(M, i):
    n = len(M)
    visited = [0 for _ in range(n)]
    q = queue.Queue()
    visited[i] = 1
    q.put(i)
    res = []
    while q.qsize() > 0:
        node = q.get()
        for neighbor in range(0, n):
            if M[node][neighbor] != 0 and visited[neighbor] != 1:
                res.append(neighbor)
                q.put(neighbor)
                visited[neighbor] = 1

    return res


def bfsl(L, N, i):
    visited = [0 for _ in range(N)]
    q = queue.Queue()
    visited[i] = 1
    q.put(i)
    res = []
    while q.qsize() > 0:
        node = q.get()
        for neighbor in L[node]:
            if visited[neighbor] != 1:
                res.append(neighbor)
                q.put(neighbor)
                visited[neighbor] = 1

    return res


def maximumLabelingM(M):
    N = len(M)
    maxL = [defaultdict(set) for _ in range(N)]

    for i in range(N):
        res = bfsm(M, i)
        for lo in res:
            maxL[i]['out'].add(lo)
            maxL[lo]['in'].add(i)
    return maxL


def maximumLabelingL(L, N):
    maxL = [defaultdict(set) for _ in range(N)]

    for i in range(N):
        #if i % 1000 == 0:
        #    print(i)
        res = bfsl(L, N, i)
        for lo in res:
            maxL[i]['out'].add(lo)
            maxL[lo]['in'].add(i)
    return maxL


def deleteM(M, maxL, u, v):
    if M[u][v] == 0:
        return
    M[u][v] = 0
    maxL[u]['out'].remove(v)
    maxL[v]['in'].remove(u)
    workset = maxL[u]['in'].copy()
    workset.add(u)
    for node in workset:
        X = set(bfsm(M, node))
        for lo in maxL[node]['out'].copy():
            if lo not in X:
                maxL[node]['out'].remove(lo)
                maxL[lo]['in'].remove(node)


def deleteL(L, maxL, N, u, v):
    if v not in maxL[u]['out']:
        return
    L[u].remove(v)
    maxL[u]['out'].remove(v)
    maxL[v]['in'].remove(u)
    workset = maxL[u]['in'].copy()
    workset.add(u)
    for node in workset:
        X = set(bfsl(L, N, node))
        for lo in maxL[node]['out'].copy():
            if lo not in X:
                maxL[node]['out'].remove(lo)
                maxL[lo]['in'].remove(node)


def insertM(M, maxL, u, v):
    if M[u][v] == 1:
        return

    M[u][v] = 1
    if v in maxL[u]['out']:
        return
    else:
        workset_in = maxL[u]['in'].copy()
        workset_in.add(u)
        workset_out = maxL[v]['out'].copy()
        workset_out.add(v)
        for li in workset_in:
            for lo in workset_out:
                if li not in maxL[lo]['in']:
                    if li != lo:
                        maxL[lo]['in'].add(li)
                        maxL[li]['out'].add(lo)


def insertL(L, maxL, u, v):
    if v in maxL[u]:
        return

    L[u].add(v)
    if v in maxL[u]['out']:
        return
    else:
        workset_in = maxL[u]['in'].copy()
        workset_in.add(u)
        workset_out = maxL[v]['out'].copy()
        workset_out.add(v)
        for li in workset_in:
            for lo in workset_out:
                if li not in maxL[lo]['in']:
                    if li != lo:
                        maxL[lo]['in'].add(li)
                        maxL[li]['out'].add(lo)
