
j.system.platform.ubuntu
========================


* path: /baselib/platforms/ubuntu/Ubuntu.py


addUser2Group
-------------


* params: group,user
* path:/baselib/platforms/ubuntu/Ubuntu.py (line:79)


changeSourceUri
---------------


* params: newuri
* path:/baselib/platforms/ubuntu/Ubuntu.py (line:287)


check
-----


* params: die
* path:/baselib/platforms/ubuntu/Ubuntu.py (line:30)


check if ubuntu or mint (which is based on ubuntu)


checkInstall
------------


* params: packagenames,cmdname
* path:/baselib/platforms/ubuntu/Ubuntu.py (line:86)



createGroup
-----------


* params: name
* path:/baselib/platforms/ubuntu/Ubuntu.py (line:74)


createUser
----------


* params: name,passwd,home,creategroup
* path:/baselib/platforms/ubuntu/Ubuntu.py (line:57)


find1packageInstalled
---------------------


* params: packagename
* path:/baselib/platforms/ubuntu/Ubuntu.py (line:274)


findPackagesInstalled
---------------------


* params: packagename
* path:/baselib/platforms/ubuntu/Ubuntu.py (line:262)


findPackagesRepo
----------------


* params: packagename
* path:/baselib/platforms/ubuntu/Ubuntu.py (line:251)


getPackage
----------


* params: name
* path:/baselib/platforms/ubuntu/Ubuntu.py (line:248)


getPackageNamesInstalled
------------------------


* params:
* path:/baselib/platforms/ubuntu/Ubuntu.py (line:239)


getPackageNamesRepo
-------------------


* params:
* path:/baselib/platforms/ubuntu/Ubuntu.py (line:236)


getVersion
----------


* params:
* path:/baselib/platforms/ubuntu/Ubuntu.py (line:47)


returns codename,descr,id,release
known ids" raring, linuxmint


initApt
-------


* params:
* path:/baselib/platforms/ubuntu/Ubuntu.py (line:10)


install
-------


* params: packagename
* path:/baselib/platforms/ubuntu/Ubuntu.py (line:106)


installDebFile
--------------


* params: path
* path:/baselib/platforms/ubuntu/Ubuntu.py (line:149)


installVersion
--------------


* params: packageName,version
* path:/baselib/platforms/ubuntu/Ubuntu.py (line:125)


Installs a specific version of an ubuntu package.




listSources
-----------


* params:
* path:/baselib/platforms/ubuntu/Ubuntu.py (line:283)


remove
------


* params: packagename
* path:/baselib/platforms/ubuntu/Ubuntu.py (line:157)


restartService
--------------


* params: servicename
* path:/baselib/platforms/ubuntu/Ubuntu.py (line:206)


serviceDisableStartAtBoot
-------------------------


* params: servicename
* path:/baselib/platforms/ubuntu/Ubuntu.py (line:217)


serviceEnableStartAtBoot
------------------------


* params: servicename
* path:/baselib/platforms/ubuntu/Ubuntu.py (line:220)


serviceInstall
--------------


* params: servicename,daemonpath,args,respawn,pwd,env,reload
* path:/baselib/platforms/ubuntu/Ubuntu.py (line:170)


serviceUninstall
----------------


* params: servicename
* path:/baselib/platforms/ubuntu/Ubuntu.py (line:190)


startService
------------


* params: servicename
* path:/baselib/platforms/ubuntu/Ubuntu.py (line:194)


statusService
-------------


* params: servicename
* path:/baselib/platforms/ubuntu/Ubuntu.py (line:209)


stopService
-----------


* params: servicename
* path:/baselib/platforms/ubuntu/Ubuntu.py (line:201)


updatePackageMetadata
---------------------


* params: force
* path:/baselib/platforms/ubuntu/Ubuntu.py (line:223)


upgradePackages
---------------


* params: force
* path:/baselib/platforms/ubuntu/Ubuntu.py (line:229)


