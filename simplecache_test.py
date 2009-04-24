import unittest
import mox
import simplecache
import pdb

class TestUnboundedCache(unittest.TestCase):
    def test_can_put_and_get_from_a_basic_cache(self):
        cache = simplecache.UnboundedCache()
        cache.put('key', 'value')
        self.assertEquals(cache.get('key'), 'value')

class TestBoundCacheWithLRUAlgorithm(unittest.TestCase):
    def test_cache_removes_least_recently_used_item_on_put(self):
        cache = simplecache.Cache(size=3, algorithm=simplecache.LRU())
        cache.put('A', 'A')
        cache.put('B', 'B')
        cache.put('C', 'C')
        self.assertEquals('A', cache.cache.get('A'))
        self.assertEquals('B', cache.cache.get('B'))
        self.assertEquals('C', cache.cache.get('C'))
        self.assertEquals(None, cache.cache.get('D'))
        cache.put('D', 'D')
        self.assertEquals(None, cache.cache.get('A'))
        self.assertEquals('B', cache.cache.get('B'))
        self.assertEquals('C', cache.cache.get('C'))
        self.assertEquals('D', cache.cache.get('D'))

    def test_cache_refreshs_items_on_get(self):
        cache = simplecache.Cache(size=3, algorithm=simplecache.LRU())
        cache.put('A', 'A')
        cache.put('B', 'B')
        cache.put('C', 'C')
        cache.get('A')
        cache.put('D', 'D')
        self.assertEquals('A', cache.cache.get('A'))
        self.assertEquals(None, cache.cache.get('B'))
        self.assertEquals('C', cache.cache.get('C'))
        self.assertEquals('D', cache.cache.get('D'))

    def test_cache_refreshs_items_on_put(self):
        cache = simplecache.Cache(size=3, algorithm=simplecache.LRU())
        cache.put('A', 'A')
        cache.put('B', 'B')
        cache.put('C', 'C')
        cache.put('A', 'Z')
        cache.put('D', 'D')
        self.assertEquals('Z', cache.cache.get('A'))
        self.assertEquals(None, cache.cache.get('B'))
        self.assertEquals('C', cache.cache.get('C'))
        self.assertEquals('D', cache.cache.get('D'))

class TestBoundCacheWithLFUAlgorithm(unittest.TestCase):
    def test_cache_removes_least_frequently_used_item_on_put(self):
        cache = simplecache.Cache(size=3, algorithm=simplecache.LFU())
        cache.put('A', 'A')
        cache.put('B', 'B')
        cache.put('C', 'C')
        self.assertEquals('A', cache.cache.get('A')) #first
        self.assertEquals('B', cache.cache.get('B'))
        self.assertEquals('C', cache.cache.get('C'))
        self.assertEquals(None, cache.cache.get('D'))
#        pdb.set_trace()
        cache.get('A')
        cache.get('C')
        cache.put('D', 'D')
        self.assertEquals('A', cache.cache.get('A')) # Second
        self.assertEquals(None, cache.cache.get('B'))
        self.assertEquals('C', cache.cache.get('C'))
        self.assertEquals('D', cache.cache.get('D'))


if __name__ == "__main__":
    unittest.main()