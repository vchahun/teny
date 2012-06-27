#!/usr/bin/env python
import sys
import lxml.etree as et

def main(lang):
    for _, element in et.iterparse(sys.stdin):
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
