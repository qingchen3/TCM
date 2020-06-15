import os


def readEpinion(folder, filename):
    reader = open(os.path.join(folder, filename), 'r')
    N = 76000
    records = []
    for line in reader:
        if '#' in line:
            continue
        nodes = line.rstrip().split('\t')
        records.append((int(nodes[0]), int(nodes[1])))

    return N, records


def readHepPh(folder, filename):
    reader = open(os.path.join(folder, filename), 'r')
    N = 34560
    records = []
    for line in reader:
        nodes = line.rstrip().split(' ')
        records.append((int(nodes[0]), int(nodes[1])))

    return N, records

def readMoreno(folder, filename):
    reader = open(os.path.join(folder, filename), 'r')
    N = 1225
    records = []
    for line in reader:
        nodes = line.rstrip().split(' ')
        records.append((int(nodes[0]), int(nodes[1])))

    return N, records