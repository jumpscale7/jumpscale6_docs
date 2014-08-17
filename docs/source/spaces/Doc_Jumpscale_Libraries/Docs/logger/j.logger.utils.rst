
j.logger.utils
==============


* path: /core/logging/LogHandler.py


Some log related utilities.


trace
-----


* params: level,enabled
* path:/core/logging/LogHandler.py (line:44)


Decorator factory. Use enabled to avoid the logging overhead when it's
not needed. Do not the tracing can *not* be enabled or disabled at
runtime.

Typical usage:

TRACING_ENABLED = True

def myFunc(arg1, arg2=12):
...



