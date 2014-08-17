
j.clients.redis
===============


* path: /baselib/redis/Redis.py




checkAllInstances
-----------------


* params:
* path:/baselib/redis/Redis.py (line:92)


configureInstance
-----------------


* params: name,port,maxram,appendonly,snapshot,slave,ismaster,passwd
* path:/baselib/redis/Redis.py (line:170)


slave example: (192.168.10.10,8888,asecret)   (ip,port,secret)


deleteInstance
--------------


* params: name
* path:/baselib/redis/Redis.py (line:158)


emptyAllInstances
-----------------


* params:
* path:/baselib/redis/Redis.py (line:103)


emptyInstance
-------------


* params: name
* path:/baselib/redis/Redis.py (line:163)


getGeventRedisClient
--------------------


* params: ipaddr,port,fromcache,password
* path:/baselib/redis/Redis.py (line:61)


getGeventRedisQueue
-------------------


* params: ipaddr,port,name,namespace,fromcache
* path:/baselib/redis/Redis.py (line:83)


getPort
-------


* params: name
* path:/baselib/redis/Redis.py (line:121)


getProcessPids
--------------


* params: name
* path:/baselib/redis/Redis.py (line:135)


getRedisClient
--------------


* params: ipaddr,port,password
* path:/baselib/redis/Redis.py (line:71)


getRedisQueue
-------------


* params: ipaddr,port,name,namespace
* path:/baselib/redis/Redis.py (line:77)


startInstance
-------------


* params: name
* path:/baselib/redis/Redis.py (line:155)


stopInstance
------------


* params: name
* path:/baselib/redis/Redis.py (line:148)


