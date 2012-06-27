#!/usr/bin/env python
import sys
import lxml.etree as et

def main(n):
    n = int(n)
    print '<?xml version="1.0" encoding="utf-8"?>'
    print '<dataset>'
    for _, element in et.iterparse(sys.stdin):
        if element.tag == 'file':
            post_id = int(element.get('id'))
            if post_id % n == 0:
                sys.stdout.write(et.tostring(element, pretty_print=True, encoding='utf8'))
    print '</dataset>'

if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.stderr.write('Usage: %s n (post_id = 0 [n])\n' % sys.argv[0])
        sys.exit(1)
    main(*sys.argv[1:])
