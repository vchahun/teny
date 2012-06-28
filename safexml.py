import lxml.etree as et

def iterparse(stream, tag=None, events=('end',)):
    it = et.iterparse(stream, events)
    prev = next(it)
    for item in it:
        yield prev
        if prev[0] == 'end' and prev[1].tag == tag:
            prev[1].clear()
            prev[1].getparent().remove(prev[1])
        prev = item
    yield prev
