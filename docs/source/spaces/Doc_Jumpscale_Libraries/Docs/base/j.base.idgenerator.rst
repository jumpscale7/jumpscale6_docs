
j.base.idgenerator
==================


* path: /core/base/idgenerator/IDGenerator.py


generic provider of id's
lives at j.idgenerator


generateGUID
------------


* params:
* path:/core/base/idgenerator/IDGenerator.py (line:48)


generate unique guid
how to use:  j.base.idgenerator.generateGUID()


generateIncrID
--------------


* params: incrTypeId,service,reset
* path:/core/base/idgenerator/IDGenerator.py (line:18)


type is like agent, job, jobstep
needs to be a unique type, can only work if application service is known
how to use:  j.base.idgenerator.generateIncrID("agent")


generateRandomInt
-----------------


* params: fromInt,toInt
* path:/core/base/idgenerator/IDGenerator.py (line:12)


how to use:  j.base.idgenerator.generateRandomInt(0,10)


getID
-----


* params: incrTypeId,objectUniqueSeedInfo,service,reset
* path:/core/base/idgenerator/IDGenerator.py (line:34)


get a unique id for an object uniquely identified
remembers previously given id's


