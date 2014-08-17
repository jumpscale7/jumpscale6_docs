
j.core.codegenerator
====================


* path: /portal/codegentools/CodeGenerator.py


generate
--------


* params: spec,type,typecheck,dieInGenCode,appserverclient,instance,redis,wsclient,codepath,classpath,returnClass,args,makeCopy
* path:/portal/codegentools/CodeGenerator.py (line:177)


param: spec is spec we want to generate from
param: type JSModel,actormethodgreenlet,enumeration,actorlocal
param: typecheck (means in generated code the types will be checked)
param: dieInGenCode  if true means in generated code we will die when something uneforeseen happens
return: dict of classes if more than 1 otherwise just the class


getActorClass
-------------


* params: appname,actor,typecheck,dieInGenCode,codepath
* path:/portal/codegentools/CodeGenerator.py (line:75)




getClassActorLocal
------------------


* params: appname,actor,typecheck,dieInGenCode
* path:/portal/codegentools/CodeGenerator.py (line:62)




getClassActorRemote
-------------------


* params: appname,actor,typecheck,dieInGenCode,instance,redis,wsclient,codepath
* path:/portal/codegentools/CodeGenerator.py (line:89)


getClassEnumeration
-------------------


* params: appname,actor,enumname,typecheck,dieInGenCode
* path:/portal/codegentools/CodeGenerator.py (line:162)




getClassJSModel
---------------


* params: appname,actor,modelname,typecheck,dieInGenCode,codepath
* path:/portal/codegentools/CodeGenerator.py (line:115)




getClassesActorMethodGreenlet
-----------------------------


* params: appname,actor,typecheck,dieInGenCode
* path:/portal/codegentools/CodeGenerator.py (line:101)


return: returns dict with key name methodname and then the class (for each method a class is generated)


getCodeEveModel
---------------


* params: appname,actor,modelname,typecheck,dieInGenCode,codepath
* path:/portal/codegentools/CodeGenerator.py (line:139)




getCodeId
---------


* params: spec,type
* path:/portal/codegentools/CodeGenerator.py (line:174)


getCodeJSModel
--------------


* params: appname,actor,modelname,typecheck,dieInGenCode,codepath
* path:/portal/codegentools/CodeGenerator.py (line:129)




removeFromMem
-------------


* params: appname,actor
* path:/portal/codegentools/CodeGenerator.py (line:35)


resetMemNonSystem
-----------------


* params:
* path:/portal/codegentools/CodeGenerator.py (line:51)


setTarget
---------


* params: target
* path:/portal/codegentools/CodeGenerator.py (line:29)


Sets the target to generate for server or client


