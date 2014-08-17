
j.application.redis
===================


* path: /baselib/credis/CRedis.py


example for pipeline
self.execute_pipeline(('SET',"test","This Should Return"),('GET',"test"))


blpop
-----


* params: key,timeout
* path:/baselib/credis/CRedis.py (line:88)


brpoplpush
----------


* params: src,dst,timeout
* path:/baselib/credis/CRedis.py (line:142)


connect
-------


* params:
* path:/baselib/credis/CRedis.py (line:51)


delete
------


* params: key
* path:/baselib/credis/CRedis.py (line:133)


eval
----


* params: script,nrkeys
* path:/baselib/credis/CRedis.py (line:153)


evalsha
-------


* params: sha,nrkeys
* path:/baselib/credis/CRedis.py (line:150)


execute
-------


* params:
* path:/baselib/credis/CRedis.py (line:64)


exists
------


* params: key
* path:/baselib/credis/CRedis.py (line:100)


expire
------


* params: key,timeout
* path:/baselib/credis/CRedis.py (line:136)


get
---


* params: key
* path:/baselib/credis/CRedis.py (line:103)


getFallBackRedis
----------------


* params:
* path:/baselib/credis/CRedis.py (line:47)


hdel
----


* params: name
* path:/baselib/credis/CRedis.py (line:121)


hdelete
-------


* params: hkey,key
* path:/baselib/credis/CRedis.py (line:118)


hexists
-------


* params: hkey,key
* path:/baselib/credis/CRedis.py (line:124)


hget
----


* params: hkey,key
* path:/baselib/credis/CRedis.py (line:112)


hgetall
-------


* params: hkey
* path:/baselib/credis/CRedis.py (line:115)


hincrby
-------


* params: name,key,amount
* path:/baselib/credis/CRedis.py (line:139)


hkeys
-----


* params: key
* path:/baselib/credis/CRedis.py (line:97)


hset
----


* params: hkey,key,value
* path:/baselib/credis/CRedis.py (line:109)


incr
----


* params: key
* path:/baselib/credis/CRedis.py (line:127)


incrby
------


* params: key,nr
* path:/baselib/credis/CRedis.py (line:130)


keys
----


* params: key
* path:/baselib/credis/CRedis.py (line:94)


llen
----


* params: key
* path:/baselib/credis/CRedis.py (line:82)


lpop
----


* params: key
* path:/baselib/credis/CRedis.py (line:91)


lrange
------


* params: name,start,end
* path:/baselib/credis/CRedis.py (line:156)


rpush
-----


* params: key,item
* path:/baselib/credis/CRedis.py (line:85)


scriptload
----------


* params: script
* path:/baselib/credis/CRedis.py (line:145)


set
---


* params: key,value
* path:/baselib/credis/CRedis.py (line:106)


