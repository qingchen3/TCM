import os
from ctypes import *
import glob
import numpy as np

def parser(data_dir, data_file):
    f = open(os.path.join(data_dir, data_file))
    count = 0
    flip = False
    block = []
    for line in f.readlines():
        if '<article' in line:
            block.append(line)
            flip = True
        elif '</article' in line:
            block.append(line)
            flip = False
            print('\n'.join(block))
            print('\n')
            count += 1
            block = []
        elif flip == True:
            block.append(line)
        else:
            pass

        if count == 200:
            break

def get_hashcodes(item):
    libfile = glob.glob('build/*/gethashcode*.so')[0]
    mylib = CDLL(libfile)
    mylib.gethashcode.argtypes = [c_char_p]
    mylib.gethashcode.restype = POINTER(c_uint * 16)
    hashcodes = mylib.gethashcode(item.encode('utf-8'))
    return [hashcode for hashcode in hashcodes.contents]

if __name__ == '__main__':
    data_dir = '/Users/qchen6/Downloads'
    data_file = 'dblp.xml'
    #parser(data_dir, data_file)
    item = 'Michael H. Böhlen'
    hashcodes = get_hashcodes(item)
    for hashcode in hashcodes:
        print(hashcode)

