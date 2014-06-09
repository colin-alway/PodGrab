#!/usr/bin/env python

import sys
import re

def main(src):
    dst = src + '.ws'
    print src, dst
    fdst = open(dst, 'w')
    with open(src) as fsrc:
        for line in fsrc:
            line = line.replace('\t', '    ')      
            fdst.write(line)
    return
    
main(sys.argv[1])

