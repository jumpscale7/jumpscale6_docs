
j.logger
========


* path: /core/logging/LogHandler.py


addConsoleLogCategory
---------------------


* params: category
* path:/core/logging/LogHandler.py (line:224)


addLogTargetLocalFS
-------------------


* params:
* path:/core/logging/LogHandler.py (line:232)


addLogTargetStdOut
------------------


* params:
* path:/core/logging/LogHandler.py (line:229)


checktargets
------------


* params:
* path:/core/logging/LogHandler.py (line:271)


only execute this every 120 secs


cleanup
-------


* params:
* path:/core/logging/LogHandler.py (line:366)


Cleanup your logs


clear
-----


* params:
* path:/core/logging/LogHandler.py (line:358)


close
-----


* params:
* path:/core/logging/LogHandler.py (line:361)


disable
-------


* params:
* path:/core/logging/LogHandler.py (line:246)


exception
---------


* params: message,level
* path:/core/logging/LogHandler.py (line:339)


Log 'message' and the current exception traceback

The current exception is retrieved automatically. There is no need to pass it.



getLogObjectFromDict
--------------------


* params: ddict
* path:/core/logging/LogHandler.py (line:165)


log
---


* params: message,level,category,tags,jid,parentjid,masterjid,private
* path:/core/logging/LogHandler.py (line:285)


send to all log targets


logTargetAdd
------------


* params: logtarget
* path:/core/logging/LogHandler.py (line:377)


Add a LogTarget object


nologger
--------


* params: func
* path:/core/logging/LogHandler.py (line:168)


Decorator to disable logging for a specific method (probably not thread safe)


nostdout
--------


* params:
* path:/core/logging/LogHandler.py (line:181)


reset
-----


* params:
* path:/core/logging/LogHandler.py (line:206)


setLogTargetLogForwarder
------------------------


* params: serverip,port
* path:/core/logging/LogHandler.py (line:235)


there will be only logging to stdout (if q.loghandler.consoleloglevel set properly)
& to the LogForwarder


