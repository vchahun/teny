# coding:utf8
import sys
import unicodedata

META_SUB = [('"', u'“”″«»'), ('\'', u'’′‘'), ('-', u'—–−­'), ('...', u'…')]
SUB = dict((c, sub) for sub, chars in META_SUB for c in chars)

def main():
    for line in sys.stdin:
        line = line.decode('utf8') # unicode
        line = line.lower() # lowercase
        line = unicodedata.normalize('NFD', line) # unicode normalize
        line = ''.join(c for c in line if unicodedata.category(c) != 'Mn') # remove diacritics
        line = ''.join(SUB.get(c, c) for c in line)
        sys.stdout.write(line.encode('utf8'))

if __name__ == '__main__':
    main()
