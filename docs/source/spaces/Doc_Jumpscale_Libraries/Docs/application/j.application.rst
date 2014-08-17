
j.application
=============


* path: /core/Application.py


connectRedis
------------


* params:
* path:/core/Application.py (line:60)


getAgentId
----------


* params:
* path:/core/Application.py (line:112)


getCPUUsage
-----------


* params:
* path:/core/Application.py (line:228)


try to get cpu usage, if it doesn't work will return 0
By default 0 for windows


getMemoryUsage
--------------


* params:
* path:/core/Application.py (line:252)


try to get memory usage, if it doesn't work will return 0i
By default 0 for windows


getUniqueMachineId
------------------


* params:
* path:/core/Application.py (line:277)


will look for network interface and return a hash calculated from lowest mac address from all physical nics


getWhoAmiStr
------------


* params:
* path:/core/Application.py (line:109)


initGrid
--------


* params:
* path:/core/Application.py (line:103)


initWhoAmI
----------


* params:
* path:/core/Application.py (line:68)


when in grid:
is gid,nid,pid


loadConfig
----------


* params:
* path:/core/Application.py (line:115)


start
-----


* params: name,appdir
* path:/core/Application.py (line:121)


Start the application

You can only stop the application with return code 0 by calling
j.Application.stop(). Don't call sys.exit yourself, don't try to run
to end-of-script, I will find you anyway!


stop
----


* params: exitcode
* path:/core/Application.py (line:161)


Stop the application cleanly using a given exitcode



