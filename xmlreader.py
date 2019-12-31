import lxml.etree as ET
import os
import numpy as np


if __name__ == '__main__':

    '''
    2476330 authors
    23,074,282 coauthor pair 
    sketch size = 42,000 X 42,000
    '''

    data_dir = '/Users/qchen6/Downloads'
    data_file = 'dblp.xml'
    dtd_file = 'dblp.dtd'
    dtd = ET.DTD(os.path.join(data_dir, dtd_file))  # read DTD

    # iterate through nodes
    coauthor_pair = 0
    for event, element in ET.iterparse(os.path.join(data_dir, data_file), dtd_validation=True):

        # print all children
        coauthors = set()
        for child in element:
            if child.tag == 'author':
                coauthors.add(child.text)
            #if child.tag == 'title':
            #    title = child.text
            #if child.tag == 'year':
            #    year = child.text
        if len(coauthors) > 1:
            coauthor_pair += (len(coauthors) * (len(coauthors) - 1)) // 2;

        '''
        for item in coauthors:
            if 'Michael H. Böhlen' in item:
                print('title:%s' % title)
                print('year:%s' %year)
                print(coauthors)
                print('\n')
                count += 1
        '''

    print("Co-author pairs count :", coauthor_pair)
