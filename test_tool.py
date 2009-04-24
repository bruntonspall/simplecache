import simplecache

def init():
    global lru, lfu
    lru = simplecache.Cache(size=3, algorithm=simplecache.LRU())
    lfu = simplecache.Cache(size=3, algorithm=simplecache.LFU())

def display():
    print lru.algorithm.q
    print lfu.algorithm.ft

def fill(s):
    for c in s:
        lfu.put(c,c)
        lru.put(c,c)

def test_cache(s):
    init()
    fill(s)
    display()
