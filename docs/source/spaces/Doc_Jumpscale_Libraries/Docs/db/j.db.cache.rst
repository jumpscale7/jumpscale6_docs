
j.db.cache
==========


* path: /baselib/lrucache/LRUCacheFactory.py


getRCache
---------


* params: nritems
* path:/baselib/lrucache/LRUCacheFactory.py (line:8)


Least-Recently-Used (LRU) cache.
Written by http://evan.prodromou.name/Software/Python/LRUCache

Instances of this class provide a least-recently-used (LRU) cache. They
emulate a Python mapping type. You can use an LRU cache more or less like
a Python dictionary, with the exception that objects you put into the
cache may be discarded before you take them out.

Some example usage::

cache = LRUCache(32) # new cache
cache'foo' <'foo'> = get_file_contents('foo') # or whatever

if 'foo' in cache: # if it's still in cache...
contents = cache'foo' <'foo'>
else:
contents = get_file_contents('foo')
cache'foo' <'foo'> = contents

print cache.size # Maximum size

print len(cache) # 0 <= len(cache) <= cache.size

cache.size = 10 # Auto-shrink on size assignment

for i in range(50): # note: larger than cache size
cachei <i> = i

if 0 not in cache: print 'Zero was discarded.'

if 42 in cache:
del cache42 <42> # Manual deletion

for j in cache:   # iterate (in LRU order)
print j, cachej <j> # iterator produces keys, not values


getRWCache
----------


* params: nrItemsReadCache,nrItemsWriteCache,maxTimeWriteCache,writermethod
* path:/baselib/lrucache/LRUCacheFactory.py (line:5)


