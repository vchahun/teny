#!/usr/bin/env python
import sys
from safexml import iterparse
from lxml.etree import tostring

def main(n):
    n = int(n)
    print '<?xml version="1.0" encoding="utf-8"?>'
    print '<dataset>'
    for _, element in iterparse(sys.stdin, 'file'):
        if element.tag == 'file':
            post_id = int(element.get('id'))
            if post_id % n == 0:
                element.tail = ''
                sys.stdout.write(tostring(element, pretty_print=True, encoding='utf8'))
    print '</dataset>'

if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.stderr.write('Usage: %s n (post_id = 0 [n])\n' % sys.argv[0])
        sys.exit(1)
    main(*sys.argv[1:])
