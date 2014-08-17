
j.tools.jail.redis.connection_pool
==================================


* path: python.zip//redis/connection.py


Generic connection pool


disconnect
----------


* params:
* path:python.zip//redis/connection.py (line:423)


Disconnects all connections in the pool


get_connection
--------------


* params: command_name
* path:python.zip//redis/connection.py (line:399)


Get a connection from the pool


make_connection
---------------


* params:
* path:python.zip//redis/connection.py (line:409)


Create a new connection


release
-------


* params: connection
* path:python.zip//redis/connection.py (line:416)


Releases the connection back to the pool


