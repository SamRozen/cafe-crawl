#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import json
import os

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Read crawled data and prints coffees.')
    parser.add_argument('files', metavar='file',
                        nargs='+', help='list of input files')
    args = parser.parse_args()
    for filename in args.files:
        if not os.path.isfile(filename):
            print 'Cannot process file %s' % filename
            continue
        f = open(filename, 'r')
        data = json.load(f)
        for item in data:
            print '%s - %s' % (item['brand'], item['name'])
        f.close()
