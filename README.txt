Simple Cache
============

:author: Michael Brunton-Spall <michael@brunton-spall.co.uk>

Introduction
------------

This code was written and designed to make understanding how a cache works, adn what the effectiveness of an algorithm is.
It may or may not be an actual usefull cache for anything that you are doing.

I use it, using the test_tool.py to show the results of the two implemented algorithms on simple test cases.
For example

::
 
  $ ipython test_tool.py
  In [1]: test_cache("ABCD")
  ['D', 'C', 'B']
  {1: ['D', 'C', 'B']}

For usage within python code, you can check the source or the pydocs, which aren't great, but I'm sure they will get better.
The basics are 

::

  cache = simplecache.Cache(size=3, algorithm=simplecache.LRU())
  cache.put(key, value)
  value = cache.get(key)

License
-------

This library is covered under the GPL version 3, please see the licence file for details
