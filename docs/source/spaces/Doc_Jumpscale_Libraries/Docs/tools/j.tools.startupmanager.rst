
j.tools.startupmanager
======================


* path: /baselib/startupmanager/StartupManager.py


addProcess
----------


* params: name,cmd,args,env,numprocesses,priority,shell,workingdir,jpackage,domain,ports,autostart,reload_signal,user,stopcmd,pid,active,check,timeoutcheck,isJSapp,upstart,processfilterstr,stats,log
* path:/baselib/startupmanager/StartupManager.py (line:562)


disableProcess
--------------


* params: domain,name
* path:/baselib/startupmanager/StartupManager.py (line:820)


enableProcess
-------------


* params: domain,name
* path:/baselib/startupmanager/StartupManager.py (line:824)


exists
------


* params: domain,name
* path:/baselib/startupmanager/StartupManager.py (line:720)


existsJPackage
--------------


* params: jpackage
* path:/baselib/startupmanager/StartupManager.py (line:741)


getDomains
----------


* params:
* path:/baselib/startupmanager/StartupManager.py (line:725)


getProcessDef
-------------


* params: domain,name,fromkey
* path:/baselib/startupmanager/StartupManager.py (line:683)


getProcessDefs
--------------


* params: domain,name,system
* path:/baselib/startupmanager/StartupManager.py (line:694)


getProcessDefs4JPackage
-----------------------


* params: jpackage
* path:/baselib/startupmanager/StartupManager.py (line:744)


getStatus
---------


* params: domain,name
* path:/baselib/startupmanager/StartupManager.py (line:794)


get status of process, True if status ok


getStatus4JPackage
------------------


* params: jpackage
* path:/baselib/startupmanager/StartupManager.py (line:788)


listProcesses
-------------


* params:
* path:/baselib/startupmanager/StartupManager.py (line:803)


load
----


* params:
* path:/baselib/startupmanager/StartupManager.py (line:676)


monitorProcess
--------------


* params: domain,name
* path:/baselib/startupmanager/StartupManager.py (line:828)


reloadProcess
-------------


* params: domain,name
* path:/baselib/startupmanager/StartupManager.py (line:836)


remove4JPackage
---------------


* params: jpackage
* path:/baselib/startupmanager/StartupManager.py (line:784)


removeProcess
-------------


* params: domain,name
* path:/baselib/startupmanager/StartupManager.py (line:776)


reset
-----


* params:
* path:/baselib/startupmanager/StartupManager.py (line:543)


restartAll
----------


* params:
* path:/baselib/startupmanager/StartupManager.py (line:770)


restartProcess
--------------


* params: domain,name
* path:/baselib/startupmanager/StartupManager.py (line:832)


startAll
--------


* params:
* path:/baselib/startupmanager/StartupManager.py (line:751)


startJPackage
-------------


* params: jpackage
* path:/baselib/startupmanager/StartupManager.py (line:732)


startProcess
------------


* params: domain,name
* path:/baselib/startupmanager/StartupManager.py (line:812)


stopJPackage
------------


* params: jpackage
* path:/baselib/startupmanager/StartupManager.py (line:736)


stopProcess
-----------


* params: domain,name
* path:/baselib/startupmanager/StartupManager.py (line:816)


