
j.tools.jail.redis
==================


* path: /baselib/redis/Redis.py


append
------


* params: key,value
* path:/baselib/redis/Redis.py (line:541)


Appends the string `'value'` to the value at `'key'`. If `'key'`
doesn't already exist, create it with a value of `'value'`.
Returns the new length of the value at `'key'`.


bgrewriteaof
------------


* params:
* path:/baselib/redis/Redis.py (line:410)


Tell the Redis server to rewrite the AOF file from data in memory.


bgsave
------


* params:
* path:/baselib/redis/Redis.py (line:414)


Tell the Redis server to save its data to disk.  Unlike save(),
this method is asynchronous and returns immediately.


bitcount
--------


* params: key,start,end
* path:/baselib/redis/Redis.py (line:549)


Returns the count of set bits in the value of `'key'`.  Optional
`'start'` and `'end'` paramaters indicate which bytes to consider


bitop
-----


* params: operation,dest
* path:/baselib/redis/Redis.py (line:563)


Perform a bitwise operation using `'operation'` between `'keys'` and
store the result in `'dest'`.


blpop
-----


* params: keys,timeout
* path:/baselib/redis/Redis.py (line:879)


LPOP a value off of the first non-empty list
named in the `'keys'` list.

If none of the lists in `'keys'` has a value to LPOP, then block
for `'timeout'` seconds, or until a value gets pushed on to one
of the lists.

If timeout is 0, then block indefinitely.


brpop
-----


* params: keys,timeout
* path:/baselib/redis/Redis.py (line:899)


RPOP a value off of the first non-empty list
named in the `'keys'` list.

If none of the lists in `'keys'` has a value to LPOP, then block
for `'timeout'` seconds, or until a value gets pushed on to one
of the lists.

If timeout is 0, then block indefinitely.


brpoplpush
----------


* params: src,dst,timeout
* path:/baselib/redis/Redis.py (line:919)


Pop a value off the tail of `'src'`, push it on the head of `'dst'`
and then return it.

This command blocks until a value is in `'src'` or until `'timeout'`
seconds elapse, whichever is first. A `'timeout'` value of 0 blocks
forever.


client_getname
--------------


* params:
* path:/baselib/redis/Redis.py (line:429)


Returns the current connection name


client_kill
-----------


* params: address
* path:/baselib/redis/Redis.py (line:421)


Disconnects the client at `'address'` (ip:port)


client_list
-----------


* params:
* path:/baselib/redis/Redis.py (line:425)


Returns a list of currently connected clients


client_setname
--------------


* params: name
* path:/baselib/redis/Redis.py (line:433)


Sets the current connection name


config_get
----------


* params: pattern
* path:/baselib/redis/Redis.py (line:437)


Return a dictionary of configuration based on the `'pattern'`


config_resetstat
----------------


* params:
* path:/baselib/redis/Redis.py (line:445)


Reset runtime statistics


config_set
----------


* params: name,value
* path:/baselib/redis/Redis.py (line:441)


Set config item `'name'` with `'value'`


dbsize
------


* params:
* path:/baselib/redis/Redis.py (line:449)


Returns the number of keys in the current database


debug_object
------------


* params: key
* path:/baselib/redis/Redis.py (line:453)


Returns version specific metainformation about a give key


decr
----


* params: name,amount
* path:/baselib/redis/Redis.py (line:570)


Decrements the value of `'key'` by `'amount'`.  If no key exists,
the value will be initialized as 0 - `'amount'`


delete
------


* params:
* path:/baselib/redis/Redis.py (line:577)


Delete one or more keys specified by `'names'`


dump
----


* params: name
* path:/baselib/redis/Redis.py (line:582)


Return a serialized version of the value stored at the specified key.
If key does not exist a nil bulk reply is returned.


echo
----


* params: value
* path:/baselib/redis/Redis.py (line:457)


Echo the string back from the server


eval
----


* params: script,numkeys
* path:/baselib/redis/Redis.py (line:1449)


Execute the LUA `'script'`, specifying the `'numkeys'` the script
will touch and the key names and argument values in `'keys_and_args'`.
Returns the result of the script.

In practice, use the object returned by `'register_script'`. This
function exists purely for Redis API completion.


evalsha
-------


* params: sha,numkeys
* path:/baselib/redis/Redis.py (line:1460)


Use the `'sha'` to execute a LUA script already registered via EVAL
or SCRIPT LOAD. Specify the `'numkeys'` the script will touch and the
key names and argument values in `'keys_and_args'`. Returns the result
of the script.

In practice, use the object returned by `'register_script'`. This
function exists purely for Redis API completion.


execute_command
---------------


* params:
* path:/baselib/redis/Redis.py (line:387)


Execute a command and return a parsed response


exists
------


* params: name
* path:/baselib/redis/Redis.py (line:589)


Returns a boolean indicating whether key `'name'` exists


expire
------


* params: name,time
* path:/baselib/redis/Redis.py (line:594)


Set an expire flag on key `'name'` for `'time'` seconds. `'time'`
can be represented by an integer or a Python timedelta object.


expireat
--------


* params: name,when
* path:/baselib/redis/Redis.py (line:603)


Set an expire flag on key `'name'`. `'when'` can be represented
as an integer indicating unix time or a Python datetime object.


flushall
--------


* params:
* path:/baselib/redis/Redis.py (line:461)


Delete all keys in all databases on the current host


flushdb
-------


* params:
* path:/baselib/redis/Redis.py (line:465)


Delete all keys in the current database


from_url
--------


* params: cls,url,db
* path:/baselib/redis/Redis.py (line:267)


Return a Redis client object configured from the given URL.

For example::

redis://username:password@localhost:6379/0

If `'db'` is None, this method will attempt to extract the database ID
from the URL path component.

Any additional keyword arguments will be passed along to the Redis
class's initializer.


get
---


* params: name
* path:/baselib/redis/Redis.py (line:612)


Return the value at key `'name'`, or None if the key doesn't exist


getDict
-------


* params: key
* path:/baselib/redis/Redis.py (line:40)


getbit
------


* params: name,offset
* path:/baselib/redis/Redis.py (line:628)


Returns a boolean indicating the value of `'offset'` in `'name'`


getrange
--------


* params: key,start,end
* path:/baselib/redis/Redis.py (line:632)


Returns the substring of the string value stored at `'key'`,
determined by the offsets `'start'` and `'end'` (both are inclusive)


getset
------


* params: name,value
* path:/baselib/redis/Redis.py (line:639)


Set the value at key `'name'` to `'value'` if key doesn't exist
Return the value at key `'name'` atomically


hdel
----


* params: name
* path:/baselib/redis/Redis.py (line:1373)


Delete `'keys'` from hash `'name'`


hexists
-------


* params: name,key
* path:/baselib/redis/Redis.py (line:1377)


Returns a boolean indicating if `'key'` exists within hash `'name'`


hget
----


* params: name,key
* path:/baselib/redis/Redis.py (line:1381)


Return the value of `'key'` within the hash `'name'`


hgetall
-------


* params: name
* path:/baselib/redis/Redis.py (line:1385)


Return a Python dict of the hash's name/value pairs


hincrby
-------


* params: name,key,amount
* path:/baselib/redis/Redis.py (line:1389)


Increment the value of `'key'` in hash `'name'` by `'amount'`


hincrbyfloat
------------


* params: name,key,amount
* path:/baselib/redis/Redis.py (line:1393)


Increment the value of `'key'` in hash `'name'` by floating `'amount'`


hkeys
-----


* params: name
* path:/baselib/redis/Redis.py (line:1399)


Return the list of keys within hash `'name'`


hlen
----


* params: name
* path:/baselib/redis/Redis.py (line:1403)


Return the number of elements in hash `'name'`


hmget
-----


* params: name,keys
* path:/baselib/redis/Redis.py (line:1433)


Returns a list of values ordered identically to `'keys'`


hmset
-----


* params: name,mapping
* path:/baselib/redis/Redis.py (line:1421)


Sets each key in the `'mapping'` dict to its corresponding value
in the hash `'name'`


hset
----


* params: name,key,value
* path:/baselib/redis/Redis.py (line:1407)


Set `'key'` to `'value'` within hash `'name'`
Returns 1 if HSET created a new field, otherwise 0


hsetnx
------


* params: name,key,value
* path:/baselib/redis/Redis.py (line:1414)


Set `'key'` to `'value'` within hash `'name'` if `'key'` does not
exist.  Returns 1 if HSETNX created a field, otherwise 0.


hvals
-----


* params: name
* path:/baselib/redis/Redis.py (line:1438)


Return the list of values within hash `'name'`


incr
----


* params: name,amount
* path:/baselib/redis/Redis.py (line:646)


Increments the value of `'key'` by `'amount'`.  If no key exists,
the value will be initialized as `'amount'`


incrby
------


* params: name,amount
* path:/baselib/redis/Redis.py (line:653)


Increments the value of `'key'` by `'amount'`.  If no key exists,
the value will be initialized as `'amount'`


incrbyfloat
-----------


* params: name,amount
* path:/baselib/redis/Redis.py (line:663)


Increments the value at key `'name'` by floating `'amount'`.
If no key exists, the value will be initialized as `'amount'`


info
----


* params: section
* path:/baselib/redis/Redis.py (line:469)


Returns a dictionary containing information about the Redis server

The `'section'` option can be used to select a specific section
of information

The section option is not supported by older versions of Redis Server,
and will generate ResponseError


keys
----


* params: pattern
* path:/baselib/redis/Redis.py (line:670)


Returns a list of keys matching `'pattern'`


lastsave
--------


* params:
* path:/baselib/redis/Redis.py (line:484)


Return a Python datetime object representing the last time the
Redis database was saved to disk


lindex
------


* params: name,index
* path:/baselib/redis/Redis.py (line:932)


Return the item from list `'name'` at position `'index'`

Negative indexes are supported and will return an item at the
end of the list


linsert
-------


* params: name,where,refvalue,value
* path:/baselib/redis/Redis.py (line:941)


Insert `'value'` in list `'name'` either immediately before or after
`'where'` <`'where'`> `'refvalue'`

Returns the new length of the list on success or -1 if `'refvalue'`
is not in the list.


llen
----


* params: name
* path:/baselib/redis/Redis.py (line:951)


Return the length of the list `'name'`


lock
----


* params: name,timeout,sleep
* path:/baselib/redis/Redis.py (line:364)


Return a new Lock object using key `'name'` that mimics
the behavior of threading.Lock.

If specified, `'timeout'` indicates a maximum life for the lock.
By default, it will remain locked until release() is called.

`'sleep'` indicates the amount of time to sleep per loop iteration
when the lock is in blocking mode and another client is currently
holding the lock.


lpop
----


* params: name
* path:/baselib/redis/Redis.py (line:955)


Remove and return the first item of the list `'name'`


lpush
-----


* params: name
* path:/baselib/redis/Redis.py (line:959)


Push `'values'` onto the head of the list `'name'`


lpushx
------


* params: name,value
* path:/baselib/redis/Redis.py (line:963)


Push `'value'` onto the head of the list `'name'` if `'name'` exists


lrange
------


* params: name,start,end
* path:/baselib/redis/Redis.py (line:967)


Return a slice of the list `'name'` between
position `'start'` and `'end'`

`'start'` and `'end'` can be negative numbers just like
Python slicing notation


lrem
----


* params: name,value,num
* path:/baselib/redis/Redis.py (line:1546)


Remove the first `'num'` occurrences of elements equal to `'value'`
from the list stored at `'name'`.

The `'num'` argument influences the operation in the following ways:
num > 0: Remove elements equal to value moving from head to tail.
num < 0: Remove elements equal to value moving from tail to head.
num = 0: Remove all elements equal to value.


lset
----


* params: name,index,value
* path:/baselib/redis/Redis.py (line:989)


Set `'position'` of list `'name'` to `'value'`


ltrim
-----


* params: name,start,end
* path:/baselib/redis/Redis.py (line:993)


Trim the list `'name'`, removing all values not within the slice
between `'start'` and `'end'`

`'start'` and `'end'` can be negative numbers just like
Python slicing notation


mget
----


* params: keys
* path:/baselib/redis/Redis.py (line:674)


Returns a list of values ordered identically to `'keys'`


move
----


* params: name,db
* path:/baselib/redis/Redis.py (line:711)


Moves the key `'name'` to a different Redis database `'db'`


mset
----


* params:
* path:/baselib/redis/Redis.py (line:681)


Sets key/values based on a mapping. Mapping can be supplied as a single
dictionary argument or as kwargs.


msetnx
------


* params:
* path:/baselib/redis/Redis.py (line:695)


Sets key/values based on a mapping if none of the keys are already set.
Mapping can be supplied as a single dictionary argument or as kwargs.
Returns a boolean indicating if the operation was successful.


object
------


* params: infotype,key
* path:/baselib/redis/Redis.py (line:491)


Return the encoding, idletime, or refcount about the key


parse_response
--------------


* params: connection,command_name
* path:/baselib/redis/Redis.py (line:402)


Parses a response from the Redis server


persist
-------


* params: name
* path:/baselib/redis/Redis.py (line:715)


Removes an expiration on `'name'`


pexpire
-------


* params: name,time
* path:/baselib/redis/Redis.py (line:719)


Set an expire flag on key `'name'` for `'time'` milliseconds.
`'time'` can be represented by an integer or a Python timedelta
object.


pexpireat
---------


* params: name,when
* path:/baselib/redis/Redis.py (line:730)


Set an expire flag on key `'name'`. `'when'` can be represented
as an integer representing unix time in milliseconds (unix time * 1000)
or a Python datetime object.


ping
----


* params:
* path:/baselib/redis/Redis.py (line:495)


Ping the Redis server


pipeline
--------


* params: transaction,shard_hint
* path:/baselib/redis/Redis.py (line:1522)


Return a new pipeline object that can queue multiple commands for
later execution. `'transaction'` indicates whether all commands
should be executed atomically. Apart from making a group of operations
atomic, pipelines are useful for reducing the back-and-forth overhead
between the client and server.


psetex
------


* params: name,time_ms,value
* path:/baselib/redis/Redis.py (line:741)


Set the value of key `'name'` to `'value'` that expires in `'time_ms'`
milliseconds. `'time_ms'` can be represented by an integer or a Python
timedelta object


pttl
----


* params: name
* path:/baselib/redis/Redis.py (line:752)


Returns the number of milliseconds until the key `'name'` will expire


publish
-------


* params: channel,message
* path:/baselib/redis/Redis.py (line:1442)


Publish `'message'` on `'channel'`.
Returns the number of subscribers the message was delivered to.


pubsub
------


* params: shard_hint
* path:/baselib/redis/Redis.py (line:378)


Return a Publish/Subscribe object. With this object, you can
subscribe to channels and listen for messages that get published to
them.


randomkey
---------


* params:
* path:/baselib/redis/Redis.py (line:756)


Returns the name of a random key


register_script
---------------


* params: script
* path:/baselib/redis/Redis.py (line:1496)


Register a LUA `'script'` specifying the `'keys'` it will touch.
Returns a Script object that is callable and hides the complexity of
deal with scripts, keys, and shas. This is the preferred way to work
with LUA scripts.


rename
------


* params: src,dst
* path:/baselib/redis/Redis.py (line:760)


Rename key `'src'` to `'dst'`


renamenx
--------


* params: src,dst
* path:/baselib/redis/Redis.py (line:766)


Rename key `'src'` to `'dst'` if `'dst'` doesn't already exist


restore
-------


* params: name,ttl,value
* path:/baselib/redis/Redis.py (line:770)


Create a key using the provided serialized value, previously obtained
using DUMP.


rpop
----


* params: name
* path:/baselib/redis/Redis.py (line:1003)


Remove and return the last item of the list `'name'`


rpoplpush
---------


* params: src,dst
* path:/baselib/redis/Redis.py (line:1007)


RPOP a value off of the `'src'` list and atomically LPUSH it
on to the `'dst'` list.  Returns the value.


rpush
-----


* params: name
* path:/baselib/redis/Redis.py (line:1014)


Push `'values'` onto the tail of the list `'name'`


rpushx
------


* params: name,value
* path:/baselib/redis/Redis.py (line:1018)


Push `'value'` onto the tail of the list `'name'` if `'name'` exists


sadd
----


* params: name
* path:/baselib/redis/Redis.py (line:1090)


Add `'value(s)'` to set `'name'`


save
----


* params:
* path:/baselib/redis/Redis.py (line:499)


Tell the Redis server to save its data to disk,
blocking until the save is complete


scard
-----


* params: name
* path:/baselib/redis/Redis.py (line:1094)


Return the number of elements in set `'name'`


script_exists
-------------


* params:
* path:/baselib/redis/Redis.py (line:1472)


Check if a script exists in the script cache by specifying the SHAs of
each script as `'args'`. Returns a list of boolean values indicating if
if each already script exists in the cache.


script_flush
------------


* params:
* path:/baselib/redis/Redis.py (line:1481)


Flush all scripts from the script cache


script_kill
-----------


* params:
* path:/baselib/redis/Redis.py (line:1486)


Kill the currently executing LUA script


script_load
-----------


* params: script
* path:/baselib/redis/Redis.py (line:1491)


Load a LUA `'script'` into the script cache. Returns the SHA.


sdiff
-----


* params: keys
* path:/baselib/redis/Redis.py (line:1098)


Return the difference of sets specified by `'keys'`


sdiffstore
----------


* params: dest,keys
* path:/baselib/redis/Redis.py (line:1103)


Store the difference of sets specified by `'keys'` into a new
set named `'dest'`.  Returns the number of keys in the new set.


sentinel
--------


* params:
* path:/baselib/redis/Redis.py (line:506)


Redis Sentinel's SENTINEL command


set
---


* params: name,value,ex,px,nx,xx
* path:/baselib/redis/Redis.py (line:777)


Set the value at key `'name'` to `'value'`

`'ex'` sets an expire flag on key `'name'` for `'ex'` seconds.

`'px'` sets an expire flag on key `'name'` for `'px'` milliseconds.

`'nx'` if set to True, set the value at key `'name'` to `'value'` if it
does not already exist.

`'xx'` if set to True, set the value at key `'name'` to `'value'` if it
already exists.


set_response_callback
---------------------


* params: command,callback
* path:/baselib/redis/Redis.py (line:327)


Set a custom Response Callback


setbit
------


* params: name,offset,value
* path:/baselib/redis/Redis.py (line:811)


Flag the `'offset'` in `'name'` as `'value'`. Returns a boolean
indicating the previous value of `'offset'`.


setex
-----


* params: name,value,time
* path:/baselib/redis/Redis.py (line:1536)


Set the value of key `'name'` to `'value'` that expires in `'time'`
seconds. `'time'` can be represented by an integer or a Python
timedelta object.


setnx
-----


* params: name,value
* path:/baselib/redis/Redis.py (line:829)


Set the value of key `'name'` to `'value'` if key doesn't exist


setrange
--------


* params: name,offset,value
* path:/baselib/redis/Redis.py (line:833)


Overwrite bytes in the value of `'name'` starting at `'offset'` with
`'value'`. If `'offset'` plus the length of `'value'` exceeds the
length of the original value, the new value will be larger than before.
If `'offset'` exceeds the length of the original value, null bytes
will be used to pad between the end of the previous value and the start
of what's being injected.

Returns the length of the new string.


shutdown
--------


* params:
* path:/baselib/redis/Redis.py (line:514)


Shutdown the server


sinter
------


* params: keys
* path:/baselib/redis/Redis.py (line:1111)


Return the intersection of sets specified by `'keys'`


sinterstore
-----------


* params: dest,keys
* path:/baselib/redis/Redis.py (line:1116)


Store the intersection of sets specified by `'keys'` into a new
set named `'dest'`.  Returns the number of keys in the new set.


sismember
---------


* params: name,value
* path:/baselib/redis/Redis.py (line:1124)


Return a boolean indicating if `'value'` is a member of set `'name'`


slaveof
-------


* params: host,port
* path:/baselib/redis/Redis.py (line:523)


Set the server to be a replicated slave of the instance identified
by the `'host'` and `'port'`. If called without arguements, the
instance is promoted to a master instead.


smembers
--------


* params: name
* path:/baselib/redis/Redis.py (line:1128)


Return all members of the set `'name'`


smove
-----


* params: src,dst,value
* path:/baselib/redis/Redis.py (line:1132)


Move `'value'` from set `'src'` to set `'dst'` atomically


sort
----


* params: name,start,num,by,get,desc,alpha,store,groups
* path:/baselib/redis/Redis.py (line:1022)


Sort and return the list, set or sorted set at `'name'`.

`'start'` and `'num'` allow for paging through the sorted data

`'by'` allows using an external key to weight and sort the items.
Use an "*" to indicate where in the key the item value is located

`'get'` allows for returning items from external keys rather than the
sorted data itself.  Use an "*" to indicate where int he key
the item value is located

`'desc'` allows for reversing the sort

`'alpha'` allows for sorting lexicographically rather than numerically

`'store'` allows for storing the result of the sort into
the key `'store'`

`'groups'` if set to True and if `'get'` contains at least two
elements, sort will return a list of tuples, each containing the
values fetched from the arguments to `'get'`.


spop
----


* params: name
* path:/baselib/redis/Redis.py (line:1136)


Remove and return a random member of set `'name'`


srandmember
-----------


* params: name,number
* path:/baselib/redis/Redis.py (line:1140)


If `'number'` is None, returns a random member of set `'name'`.

If `'number'` is supplied, returns a list of `'number'` random
memebers of set `'name'`. Note this is only available when running
Redis 2.6+.


srem
----


* params: name
* path:/baselib/redis/Redis.py (line:1151)


Remove `'values'` from set `'name'`


strlen
------


* params: name
* path:/baselib/redis/Redis.py (line:846)


Return the number of bytes stored in the value of `'name'`


substr
------


* params: name,start,end
* path:/baselib/redis/Redis.py (line:850)


Return a substring of the string at key `'name'`. `'start'` and `'end'`
are 0-based integers specifying the portion of the string to return.


sunion
------


* params: keys
* path:/baselib/redis/Redis.py (line:1155)


Return the union of sets specifiued by `'keys'`


sunionstore
-----------


* params: dest,keys
* path:/baselib/redis/Redis.py (line:1160)


Store the union of sets specified by `'keys'` into a new
set named `'dest'`.  Returns the number of keys in the new set.


time
----


* params:
* path:/baselib/redis/Redis.py (line:533)


Returns the server time as a 2-item tuple of ints:
(seconds since epoch, microseconds into this second).


transaction
-----------


* params: func
* path:/baselib/redis/Redis.py (line:345)


Convenience method for executing the callable 'func' as a transaction
while watching all keys specified in 'watches'. The 'func' callable
should expect a single arguement which is a Pipeline object.


ttl
---


* params: name
* path:/baselib/redis/Redis.py (line:857)


Returns the number of seconds until the key `'name'` will expire


type
----


* params: name
* path:/baselib/redis/Redis.py (line:861)


Returns the type of key `'name'`


unwatch
-------


* params:
* path:/baselib/redis/Redis.py (line:871)


Unwatches the value at key `'name'`, or None of the key doesn't exist


watch
-----


* params:
* path:/baselib/redis/Redis.py (line:865)


Watches the values at keys `'names'`, or None if the key doesn't exist


zadd
----


* params: name
* path:/baselib/redis/Redis.py (line:1558)


NOTE: The order of arguments differs from that of the official ZADD
command. For backwards compatability, this method accepts arguments
in the form of name1, score1, name2, score2, while the official Redis
documents expects score1, name1, score2, name2.

If you're looking to use the standard syntax, consider using the
StrictRedis class. See the API Reference section of the docs for more
information.

Set any number of element-name, score pairs to the key `'name'`. Pairs
can be specified in two ways:

As *args, in the form of: name1, score1, name2, score2, ...
or as **kwargs, in the form of: name1=score1, name2=score2, ...

The following example would add four values to the 'my-key' key:
redis.zadd('my-key', 'name1', 1.1, 'name2', 2.2, name3=3.3, name4=4.4)


zcard
-----


* params: name
* path:/baselib/redis/Redis.py (line:1191)


Return the number of elements in the sorted set `'name'`


zcount
------


* params: name,min,max
* path:/baselib/redis/Redis.py (line:1195)


Returns the number of elements in the sorted set at key `'name'` with
a score between `'min'` and `'max'`.


zincrby
-------


* params: name,value,amount
* path:/baselib/redis/Redis.py (line:1202)


Increment the score of `'value'` in sorted set `'name'` by `'amount'`


zinterstore
-----------


* params: dest,keys,aggregate
* path:/baselib/redis/Redis.py (line:1206)


Intersect multiple sorted sets specified by `'keys'` into
a new sorted set, `'dest'`. Scores in the destination will be
aggregated based on the `'aggregate'`, or SUM if none is provided.


zrange
------


* params: name,start,end,desc,withscores,score_cast_func
* path:/baselib/redis/Redis.py (line:1214)


Return a range of values from sorted set `'name'` between
`'start'` and `'end'` sorted in ascending order.

`'start'` and `'end'` can be negative, indicating the end of the range.

`'desc'` a boolean indicating whether to sort the results descendingly

`'withscores'` indicates to return the scores along with the values.
The return type is a list of (value, score) pairs

`'score_cast_func'` a callable used to cast the score return value


zrangebyscore
-------------


* params: name,min,max,start,num,withscores,score_cast_func
* path:/baselib/redis/Redis.py (line:1239)


Return a range of values from the sorted set `'name'` with scores
between `'min'` and `'max'`.

If `'start'` and `'num'` are specified, then return a slice
of the range.

`'withscores'` indicates to return the scores along with the values.
The return type is a list of (value, score) pairs

'score_cast_func'` a callable used to cast the score return value


zrank
-----


* params: name,value
* path:/baselib/redis/Redis.py (line:1265)


Returns a 0-based value indicating the rank of `'value'` in sorted set
`'name'`


zrem
----


* params: name
* path:/baselib/redis/Redis.py (line:1272)


Remove member `'values'` from sorted set `'name'`


zremrangebyrank
---------------


* params: name,min,max
* path:/baselib/redis/Redis.py (line:1276)


Remove all elements in the sorted set `'name'` with ranks between
`'min'` and `'max'`. Values are 0-based, ordered from smallest score
to largest. Values can be negative indicating the highest scores.
Returns the number of elements removed


zremrangebyscore
----------------


* params: name,min,max
* path:/baselib/redis/Redis.py (line:1285)


Remove all elements in the sorted set `'name'` with scores
between `'min'` and `'max'`. Returns the number of elements removed.


zrevrange
---------


* params: name,start,num,withscores,score_cast_func
* path:/baselib/redis/Redis.py (line:1292)


Return a range of values from sorted set `'name'` between
`'start'` and `'num'` sorted in descending order.

`'start'` and `'num'` can be negative, indicating the end of the range.

`'withscores'` indicates to return the scores along with the values
The return type is a list of (value, score) pairs

`'score_cast_func'` a callable used to cast the score return value


zrevrangebyscore
----------------


* params: name,max,min,start,num,withscores,score_cast_func
* path:/baselib/redis/Redis.py (line:1312)


Return a range of values from the sorted set `'name'` with scores
between `'min'` and `'max'` in descending order.

If `'start'` and `'num'` are specified, then return a slice
of the range.

`'withscores'` indicates to return the scores along with the values.
The return type is a list of (value, score) pairs

`'score_cast_func'` a callable used to cast the score return value


zrevrank
--------


* params: name,value
* path:/baselib/redis/Redis.py (line:1338)


Returns a 0-based value indicating the descending rank of
`'value'` in sorted set `'name'`


zscore
------


* params: name,value
* path:/baselib/redis/Redis.py (line:1345)


Return the score of element `'value'` in sorted set `'name'`


zunionstore
-----------


* params: dest,keys,aggregate
* path:/baselib/redis/Redis.py (line:1349)


Union multiple sorted sets specified by `'keys'` into
a new sorted set, `'dest'`. Scores in the destination will be
aggregated based on the `'aggregate'`, or SUM if none is provided.


