
j.core.osis
===========


* path: /grid/osis/OSISFactory.py




decrypt
-------


* params: val,json
* path:/grid/osis/OSISFactory.py (line:89)


encrypt
-------


* params: obj
* path:/grid/osis/OSISFactory.py (line:76)


generateOsisModelDefaults
-------------------------


* params: namespace,specpath
* path:/grid/osis/OSISFactory.py (line:271)


getClient
---------


* params: ipaddr,port,user,passwd,ssl,gevent
* path:/grid/osis/OSISFactory.py (line:127)


getClientByInstance
-------------------


* params: instance,ssl,gevent
* path:/grid/osis/OSISFactory.py (line:169)


getClientForCategory
--------------------


* params: client,namespace,category
* path:/grid/osis/OSISFactory.py (line:186)


how to use

client=j.core.osis.getClient("localhost",port=5544,user="root",passwd="rooter",ssl=False)
client4node=j.core.osis.getClientForCategory(client,"system","node")


getClientForNamespace
---------------------


* params: namespace,client
* path:/grid/osis/OSISFactory.py (line:181)


getLocal
--------


* params: path,overwriteHRD,overwriteImplementation,namespacename
* path:/grid/osis/OSISFactory.py (line:98)


create local instance starting from path


getModelTemplate
----------------


* params:
* path:/grid/osis/OSISFactory.py (line:283)


getOSISBaseObjectComplexType
----------------------------


* params:
* path:/grid/osis/OSISFactory.py (line:200)


getOsisBaseObjectClass
----------------------


* params:
* path:/grid/osis/OSISFactory.py (line:197)


getOsisImplementationParentClass
--------------------------------


* params: namespacename
* path:/grid/osis/OSISFactory.py (line:203)


return parent class for osis implementation (is the implementation from which each namespace & category inherits)


getOsisModelClass
-----------------


* params: namespace,category,specpath
* path:/grid/osis/OSISFactory.py (line:288)


returns class generated from spec file or from model.py file


startDaemon
-----------


* params: path,overwriteHRD,overwriteImplementation,key,port,superadminpasswd,dbconnections,hrd
* path:/grid/osis/OSISFactory.py (line:106)


start deamon


