# coding:utf8
import sys
from safexml import iterparse
from lxml.etree import tostring

ASCII = unicode(''.join(chr(c) for c in range(32, 127)))
ACCENTS = u'àáâãäèéêëìíîïòóôõöúùüñn̈ç'
PUNCT = u'“”″«»’′‘°€¢¥£©§—–−­…'
CHARS = set(ASCII+ACCENTS+ACCENTS.upper()+PUNCT)

def should_keep(text):
    return all(c in CHARS for c in text)

def main():
    print '<?xml version="1.0" encoding="utf-8"?>'
    print '<dataset>'
    for _, element in iterparse(sys.stdin, 'file'):
        if element.tag == 's':
            keep = should_keep(element.text.replace(u'\xa0', u' '))
        elif element.tag == 'unit':
            if not keep:
                element.getparent().remove(element)
        if element.tag == 'file':
            element.tail = ''
            sys.stdout.write(tostring(element, pretty_print=True, encoding='utf8'))
    print '</dataset>'

if __name__ == '__main__':
    main()
