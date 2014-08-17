
j.enumerators.MessageType
=========================


* path: /core/enumerators/MessageType.py


iterator for types of messages
- logmessage
- errorcondition, e.g.
- bug in application (a raised error by jumpscale)
- cpu overloaded (detected by monitoring tasklet)
- testresult e.g. avgcpu over last 1h
- job message e.g. tells information about object
- JSModel update message
- rpc message
more info see:
- http://www.jumpscale.org/display/PM/JumpScale+Messages
- http://www.jumpscale.org/display/PM/MessageTypes


check
-----


* params: cls,value
* path:/core/enumerators/MessageType.py (line:404)


Type check for this enumeration type

This method checks whether the provided argument value is an instance
of this enumeration type and is registered on it.



getByLevel
----------


* params: cls,level
* path:/core/enumerators/MessageType.py (line:374)


Get enumeration value based on item level as provided to L{registerItem}
only works for enumeration where level has been defined


getByName
---------


* params: cls,itemname
* path:/core/enumerators/MessageType.py (line:366)


Get enumeration value based on item name as provided to L{registerItem}


printdoc
--------


* params:
* path:/core/enumerators/MessageType.py (line:419)


