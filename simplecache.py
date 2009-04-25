class LRU:
    """ An algorithm for use with a cache.  Evicts the item that was least recently used """
    def __init__(self):
        self.q = []
    def _relink(self, key):
        if key in self.q:
            self.q.remove(key)
        self.q.insert(0, key)
    def register_get(self, key):
        self._relink(key)
    def register_put(self, key, value):
        self._relink(key)
    def evict(self, cache):
        cache._remove(self.q.pop())

class LFU:
    """ An algorithm for use with a cache.  Evicts the item that is least frequently used """
    def __init__(self):
        self.ft = {}
        self.lookup = {}
        self.size = 0
    def _link(self, freq, key, value):
        self.lookup[key] = freq
        if freq in self.ft:
            self.ft[freq].insert(0, value)
        else:
            self.ft[freq] = [value]
        self.size += 1
    def _unlink(self, freq, key=None):
        self.size -= 1
        if key == None:
            key = self.ft[freq].pop()
        else:
            self.ft[freq].remove(key)
        del self.lookup[key]

        return key        
    def _relink(self, key):
        f = self.lookup[key]
        value = self._unlink(f, key)
        self._link(f+1, key, value)
        return value
    def register_get(self, key):
        if key in self.lookup:
            return self._relink(key)
        else:
            return None
    def register_put(self, key, value):
        if key in self.lookup:
            f = self.lookup.get(key)
            self._unlink(f, key)
            self._link(f+1, key, value)
        else:
            self._link(1, key, value)

    def evict(self, cache):
        for f in self.ft:
            if len(self.ft[f]) > 0:
                key = self._unlink(f)
                return cache._remove(key)

class UnboundedCache:
    """ An unbounded cache that will grow forever """
    def __init__(self):
        self.cache = {}
    def get(self, key):
        if key in self.cache:
            return self.cache[key]
        return None
    def put(self, key, value):
        self.cache[key] = value

class MaxSizeCache:
    """ A bound cache, which when it's size is greater than a fixed size, executes the eviction algorithm """
    def __init__(self, size=5, algorithm=None):
        self.cache = {}
        self.maxsize = size
        if algorithm == None:
            algorithm = LRU()
        self.algorithm = algorithm
    def get(self, key):
        if key in self.cache:
            self.algorithm.register_get(key)
            return self.cache[key]
        return None
    def put(self, key, value):
        if len(self.cache) == self.maxsize:
            self.algorithm.evict(self)
        self.algorithm.register_put(key, value)
        self.cache[key] = value
    def _remove(self, key):
        del self.cache[key]

Cache = MaxSizeCache
