import os


def readTest(folder, filename):
    reader = open(os.path.join(folder, filename), 'r')
    N = 10
    records = []
    for line in reader:
        nodes = line.rstrip().split(' ')
        records.append((int(nodes[0]), int(nodes[1])))

    return N, records

def readChicagoRegional(folder, filename):
    reader = open(os.path.join(folder, filename), 'r')
    N = 1468
    records = []
    for line in reader:
        if '%' in line:
            continue
        nodes = line.rstrip().split(' ')
        records.append((int(nodes[0]), int(nodes[1])))
        records.append((int(nodes[1]), int(nodes[0])))

    return N, records

def readAirTraffic(folder, filename):
    reader = open(os.path.join(folder, filename), 'r')
    N = 1227
    records = []
    for line in reader:
        if '%' in line:
            continue
        nodes = line.rstrip().split(' ')
        records.append((int(nodes[0]), int(nodes[1])))

    return N, records


def readUSAirport(folder, filename):
    reader = open(os.path.join(folder, filename), 'r')
    N = 1580
    records = []
    for line in reader:
        if '%' in line:
            continue
        nodes = line.rstrip().split(' ')
        records.append((int(nodes[0]), int(nodes[1])))

    return N, records


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

def readMorenoHighSchool(folder, filename):
    reader = open(os.path.join(folder, filename), 'r')
    N = 71
    records = []
    for line in reader:
        if '%' in line:
            continue
        nodes = line.rstrip().split(' ')
        records.append((int(nodes[0]), int(nodes[1])))

    return N, records