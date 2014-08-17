
j.events
========


* path: /core/errorhandling/EventHandler.py


bug_critical
------------


* params: msg,category,jobid,e
* path:/core/errorhandling/EventHandler.py (line:5)


will die


bug_warning
-----------


* params: msg,category,e
* path:/core/errorhandling/EventHandler.py (line:20)


will die


inputerror_critical
-------------------


* params: msg,category,msgpub
* path:/core/errorhandling/EventHandler.py (line:50)


will die


inputerror_warning
------------------


* params: msg,category,msgpub
* path:/core/errorhandling/EventHandler.py (line:56)


will die


opserror
--------


* params: msg,category,e
* path:/core/errorhandling/EventHandler.py (line:39)


will NOT die
will make warning event is the same as opserror_warning


opserror_critical
-----------------


* params: msg,category
* path:/core/errorhandling/EventHandler.py (line:30)


will die


opserror_warning
----------------


* params: msg,category,e
* path:/core/errorhandling/EventHandler.py (line:39)


will NOT die
will make warning event is the same as opserror_warning


