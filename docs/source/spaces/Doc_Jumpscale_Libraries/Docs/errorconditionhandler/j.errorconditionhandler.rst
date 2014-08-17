
j.errorconditionhandler
=======================


* path: /core/errorhandling/ErrorConditionHandler.py


checkErrorIgnore
----------------


* params: eco
* path:/core/errorhandling/ErrorConditionHandler.py (line:339)


escalateBugToDeveloper
----------------------


* params: errorConditionObject,tb
* path:/core/errorhandling/ErrorConditionHandler.py (line:646)


excepthook
----------


* params: ttype,pythonExceptionObject,tb
* path:/core/errorhandling/ErrorConditionHandler.py (line:308)


every fatal error in jumpscale or by python itself will result in an exception
in this function the exception is caught.
This routine will create an errorobject & escalate to the infoserver


getErrorConditionObject
-----------------------


* params: ddict,msg,msgpub,category,level,type,tb
* path:/core/errorhandling/ErrorConditionHandler.py (line:179)


returns only ErrorConditionObject which should be used in jumpscale to define an errorcondition (or potential error condition)


getErrorTraceKIS
----------------


* params: tb
* path:/core/errorhandling/ErrorConditionHandler.py (line:394)


getFrames
---------


* params: tb
* path:/core/errorhandling/ErrorConditionHandler.py (line:351)


halt
----


* params: msg
* path:/core/errorhandling/ErrorConditionHandler.py (line:730)


lastActionClear
---------------


* params:
* path:/core/errorhandling/ErrorConditionHandler.py (line:640)


clear last action so is not printed when error


lastActionSet
-------------


* params: lastActionDescription
* path:/core/errorhandling/ErrorConditionHandler.py (line:634)


will remember action you are doing, this will be added to error message if filled in


parsePythonErrorObject
----------------------


* params: pythonExceptionObject,ttype,tb,level,message
* path:/core/errorhandling/ErrorConditionHandler.py (line:210)


how to use

try:
except Exception,e:
eco=j.errorconditionhandler.parsePythonErrorObject(e)

eco is jumpscale internal format for an error
next step could be to process the error objecect (eco) e.g. by j.errorconditionhandler.processErrorConditionObject(eco)




parsepythonExceptionObject
--------------------------


* params:
* path:/core/errorhandling/ErrorConditionHandler.py (line:305)


processErrorConditionObject
---------------------------


* params: errorConditionObject,tostdout,sentry,modulename,centralsentry
* path:/core/errorhandling/ErrorConditionHandler.py (line:420)


a errorObject gets processed which means stored locally or forwarded to a logserver or both

you can overrule this behaviour by changing at rutime this function with a new one e.g. following code could work

def myProcessErrorConditionObject(eco):
print eco

j.errorconditionhandler.processErrorConditionObject=myProcessErrorConditionObject

now there would be no further processing appart from priting the errorcondition object (eco)


processPythonExceptionObject
----------------------------


* params: pythonExceptionObject,ttype,tb,level,message,sentry
* path:/core/errorhandling/ErrorConditionHandler.py (line:188)


how to use

try:
except Exception,e:
j.errorconditionhandler.processpythonExceptionObject(e)



the errorcondition is then also processed e.g. send to local logserver and/or stored locally in errordb
see j.errorconditionhandler.processErrorConditionObject how to use this and overrule the behaviour


raiseBug
--------


* params: message,category,pythonExceptionObject,pythonTraceBack,msgpub,die,tags,level
* path:/core/errorhandling/ErrorConditionHandler.py (line:52)


use this to raise a bug in the code, this is the only time that a stacktrace will be asked for
level will be Critical

try:
except Exception,e:
j.errorconditionhandler.raiseBug("an error",category="exceptions.init",e)


raiseCritical
-------------


* params: message,category,pythonExceptionObject,pythonTraceBack,msgpub,die,tags,level
* path:/core/errorhandling/ErrorConditionHandler.py (line:52)


use this to raise a bug in the code, this is the only time that a stacktrace will be asked for
level will be Critical

try:
except Exception,e:
j.errorconditionhandler.raiseBug("an error",category="exceptions.init",e)


raiseInputError
---------------


* params: message,category,msgpub,die,backtrace,tags
* path:/core/errorhandling/ErrorConditionHandler.py (line:145)


raiseMonitoringError
--------------------


* params: message,category,msgpub,die,tags
* path:/core/errorhandling/ErrorConditionHandler.py (line:164)


raiseOperationalCritical
------------------------


* params: message,category,msgpub,die,tags,eco,extra
* path:/core/errorhandling/ErrorConditionHandler.py (line:91)


use this to raise an operational issue about the system


raiseOperationalWarning
-----------------------


* params: message,category,msgpub,tags,eco
* path:/core/errorhandling/ErrorConditionHandler.py (line:134)


raisePerformanceError
---------------------


* params: message,category,msgpub,tags
* path:/core/errorhandling/ErrorConditionHandler.py (line:172)


raiseRuntimeErrorWithEco
------------------------


* params: eco,tostdout
* path:/core/errorhandling/ErrorConditionHandler.py (line:122)


raiseWarning
------------


* params: message,category,pythonExceptionObject,pythonTraceBack,msgpub,tags
* path:/core/errorhandling/ErrorConditionHandler.py (line:74)


use this to raise a bug in the code, this is the only time that a stacktrace will be asked for

try:
except Exception,e:
j.errorconditionhandler.raiseBug("an error",category="exceptions.init",e)


reRaiseECO
----------


* params: eco
* path:/core/errorhandling/ErrorConditionHandler.py (line:293)


sendEcoToSentry
---------------


* params: eco,modulename,hrdprefix
* path:/core/errorhandling/ErrorConditionHandler.py (line:474)


sendMessageToSentry
-------------------


* params: modulename,message,ttype,tags,extra,level,tb,frames,backtrace,hrdprefix
* path:/core/errorhandling/ErrorConditionHandler.py (line:504)


fatal
error
warning
info
debug


setExceptHook
-------------


* params:
* path:/core/errorhandling/ErrorConditionHandler.py (line:34)


toolStripNonAsciFromText
------------------------


* params: text
* path:/core/errorhandling/ErrorConditionHandler.py (line:31)


