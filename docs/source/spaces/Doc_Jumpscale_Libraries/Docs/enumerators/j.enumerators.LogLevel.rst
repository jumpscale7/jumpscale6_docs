
j.enumerators.LogLevel
======================


* path: /core/enumerators/LogLevel.py


Iterrator for levels of log
1: end user message
2: operator message
3: stdout
4: stderr
5: tracing 1 and/or backtrace python
6: tracing 2
7: tracing 3
8: tracing 4
9: tracing 5
10: special level, is the marker level


check
-----


* params: cls,value
* path:/core/enumerators/LogLevel.py (line:404)


Type check for this enumeration type

This method checks whether the provided argument value is an instance
of this enumeration type and is registered on it.



getByLevel
----------


* params: cls,level
* path:/core/enumerators/LogLevel.py (line:374)


Get enumeration value based on item level as provided to L{registerItem}
only works for enumeration where level has been defined


getByName
---------


* params: cls,itemname
* path:/core/enumerators/LogLevel.py (line:366)


Get enumeration value based on item name as provided to L{registerItem}


printdoc
--------


* params:
* path:/core/enumerators/LogLevel.py (line:419)


