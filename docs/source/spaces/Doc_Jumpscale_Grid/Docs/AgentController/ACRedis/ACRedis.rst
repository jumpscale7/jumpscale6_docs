

Agent controller usage of redis
*******************************

webdis based
============

webdis is webfrontend for redis and hosted on port 7779.
redis behind is on port 7770
you can use the excelent http://redisdesktop.com/ to visualize redis.

webdis only allows certain actions to make it secure

webdis default configuration



.. code-block:: python

  {
      "redis_host":   "127.0.0.1",
  
      "redis_port":   7770,
      "redis_auth":   null,
  
      "http_host":    "0.0.0.0",
      "http_port":    7779,
  
      "threads":  5,
      "pool_size": 20,
  
      "daemonize":    false,
      "websockets":   false,
  
      "database": 0,
  
      "acl": [
          {
              "enabled":  ["GET","SET", "DEL","HGET","HSET", "HDEL","EXISTS", "HEXISTS","PING"]
          }
      ],
  
          "verbosity": 6,
          "logfile": "/opt/jumpscale/var/webdis/webdis.log"
  }



structure in database
---------------------



