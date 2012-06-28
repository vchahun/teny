#!/usr/bin/env python
import sys
from safexml import iterparse

def main(lang):
    for _, element in iterparse(sys.stdin, 'file'):
        if element.tag == 's':
            sentence = element.text
        elif element.tag == 'text':
            if element.get('langid') == lang:
                print sentence.encode('utf8')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.stderr.write('Usage: %s [mlg|eng]\n' % sys.argv[0])
        sys.exit(1)
    main(*sys.argv[1:])
