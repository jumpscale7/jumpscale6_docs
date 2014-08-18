
j.tools.startupmanager
======================


* path: /baselib/startupmanager/StartupManager.py


addProcess
----------


* params: name,cmd,args,env,numprocesses,priority,shell,workingdir,jpackage,domain,ports,autostart,reload_signal,user,stopcmd,pid,active,check,timeoutcheck,isJSapp,upstart,processfilterstr,stats,log
* path:/baselib/startupmanager/StartupManager.py (line:565)


disableProcess
--------------


* params: domain,name
* path:/baselib/startupmanager/StartupManager.py (line:823)


enableProcess
-------------


* params: domain,name
* path:/baselib/startupmanager/StartupManager.py (line:827)


exists
------


* params: domain,name
* path:/baselib/startupmanager/StartupManager.py (line:723)


existsJPackage
--------------


* params: jpackage
* path:/baselib/startupmanager/StartupManager.py (line:744)


getDomains
----------


* params:
* path:/baselib/startupmanager/StartupManager.py (line:728)


getProcessDef
-------------


* params: domain,name,fromkey
* path:/baselib/startupmanager/StartupManager.py (line:686)


getProcessDefs
--------------


* params: domain,name,system
* path:/baselib/startupmanager/StartupManager.py (line:697)


getProcessDefs4JPackage
-----------------------


* params: jpackage
* path:/baselib/startupmanager/StartupManager.py (line:747)


getStatus
---------


* params: domain,name
* path:/baselib/startupmanager/StartupManager.py (line:797)


get status of process, True if status ok


getStatus4JPackage
------------------


* params: jpackage
* path:/baselib/startupmanager/StartupManager.py (line:791)


listProcesses
-------------


* params:
* path:/baselib/startupmanager/StartupManager.py (line:806)


load
----


* params:
* path:/baselib/startupmanager/StartupManager.py (line:679)


monitorProcess
--------------


* params: domain,name
* path:/baselib/startupmanager/StartupManager.py (line:831)


reloadProcess
-------------


* params: domain,name
* path:/baselib/startupmanager/StartupManager.py (line:839)


remove4JPackage
---------------


* params: jpackage
* path:/baselib/startupmanager/StartupManager.py (line:787)


removeProcess
-------------


* params: domain,name
* path:/baselib/startupmanager/StartupManager.py (line:779)


reset
-----


* params:
* path:/baselib/startupmanager/StartupManager.py (line:543)


restartAll
----------


* params:
* path:/baselib/startupmanager/StartupManager.py (line:773)


restartProcess
--------------


* params: domain,name
* path:/baselib/startupmanager/StartupManager.py (line:835)


startAll
--------


* params:
* path:/baselib/startupmanager/StartupManager.py (line:754)


startJPackage
-------------


* params: jpackage
* path:/baselib/startupmanager/StartupManager.py (line:735)


startProcess
------------


* params: domain,name
* path:/baselib/startupmanager/StartupManager.py (line:815)


stopJPackage
------------


* params: jpackage
* path:/baselib/startupmanager/StartupManager.py (line:739)


stopProcess
-----------


* params: domain,name
* path:/baselib/startupmanager/StartupManager.py (line:819)


