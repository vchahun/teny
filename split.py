#!/usr/bin/env python
import sys
from safexml import iterparse
from lxml.etree import tostring

def main(from_day, to_day):
    print '<?xml version="1.0" encoding="utf-8"?>'
    print '<dataset>'
    keep = False
    for _, element in iterparse(sys.stdin, 'file'):
        if element.tag == 'file' and keep:
            element.tail = ''
            sys.stdout.write(tostring(element, pretty_print=True, encoding='utf8'))
        elif element.tag == 'metadata':
            date = element.get('date')
            keep = (from_day <= date.split('-')[-1] <= to_day)
    print '</dataset>'

if __name__ == '__main__':
    if len(sys.argv) != 3:
        sys.stderr.write('Usage: %s from_day to_day\n' % sys.argv[0])
        sys.exit(1)
    main(*sys.argv[1:])
