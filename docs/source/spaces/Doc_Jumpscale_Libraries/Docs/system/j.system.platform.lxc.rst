
j.system.platform.lxc
=====================


* path: /lib/lxc/Lxc.py


btrfsSubvolCopy
---------------


* params: nameFrom,NameDest
* path:/lib/lxc/Lxc.py (line:176)


btrfsSubvolDelete
-----------------


* params: name
* path:/lib/lxc/Lxc.py (line:189)


btrfsSubvolExists
-----------------


* params: name
* path:/lib/lxc/Lxc.py (line:184)


btrfsSubvolList
---------------


* params:
* path:/lib/lxc/Lxc.py (line:158)


btrfsSubvolNew
--------------


* params: name
* path:/lib/lxc/Lxc.py (line:171)


create
------


* params: name,stdout,base,start,nameserver,replace
* path:/lib/lxc/Lxc.py (line:258)



destroy
-------


* params: name
* path:/lib/lxc/Lxc.py (line:370)


destroyAll
----------


* params:
* path:/lib/lxc/Lxc.py (line:364)


execute
-------


* params: command
* path:/lib/lxc/Lxc.py (line:16)


exportRsync
-----------


* params: name,backupname,key
* path:/lib/lxc/Lxc.py (line:139)


exportTgz
---------


* params: name,backupname
* path:/lib/lxc/Lxc.py (line:236)


getConfig
---------


* params: name
* path:/lib/lxc/Lxc.py (line:85)


getIp
-----


* params: name,fail
* path:/lib/lxc/Lxc.py (line:81)


getPid
------


* params: name,fail
* path:/lib/lxc/Lxc.py (line:94)


getProcessList
--------------


* params: name,stdout
* path:/lib/lxc/Lxc.py (line:108)


last one is sum of mem & cpu


importRsync
-----------


* params: backupname,name,basename,key
* path:/lib/lxc/Lxc.py (line:206)



importTgz
---------


* params: backupname,name
* path:/lib/lxc/Lxc.py (line:248)


list
----


* params:
* path:/lib/lxc/Lxc.py (line:54)


names of running & stopped machines


networkSet
----------


* params: machinename,netname,pubips,bridge,gateway
* path:/lib/lxc/Lxc.py (line:427)


networkSetPrivateVXLan
----------------------


* params: name,vxlanid,ipaddresses
* path:/lib/lxc/Lxc.py (line:468)


pushSSHKey
----------


* params: name
* path:/lib/lxc/Lxc.py (line:357)


removeRedundantFiles
--------------------


* params: name
* path:/lib/lxc/Lxc.py (line:199)


setHostName
-----------


* params: name
* path:/lib/lxc/Lxc.py (line:347)


start
-----


* params: name,stdout,test
* path:/lib/lxc/Lxc.py (line:393)


stop
----


* params: name
* path:/lib/lxc/Lxc.py (line:388)


