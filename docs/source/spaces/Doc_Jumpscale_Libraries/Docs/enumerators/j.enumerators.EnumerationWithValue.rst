
j.enumerators.EnumerationWithValue
==================================


* path: /core/baseclasses/BaseEnumeration.py


Enumeration base type providing separation between item name and value

Since some names (which are invalid Python identifiers) are forbidden as
enumeration item name, this class provides separation between item names
and item value (which is the value returned by __str__, equal to name in
the basic Enumeration type).

Next to this, it offers a 'doc' attribute which is returned by __repr__.

Example use case: the VirtualboxNicType enumeration contains an item which
should be called '82540EM'. This is an invalid identifier, so it had to be
renamed to 'I82540EM' as name. We still want to provide the original value
as well though.
Next to this, '82540EM' is not easy to understand, so we want to represent
the item as 'Intel PRO/1000MT Desktop' to the end-user, which is the doc
property displayed by __repr__.


check
-----


* params: cls,value
* path:/core/baseclasses/BaseEnumeration.py (line:404)


Type check for this enumeration type

This method checks whether the provided argument value is an instance
of this enumeration type and is registered on it.



getByLevel
----------


* params: cls,level
* path:/core/baseclasses/BaseEnumeration.py (line:374)


Get enumeration value based on item level as provided to L{registerItem}
only works for enumeration where level has been defined


getByName
---------


* params: cls,itemname
* path:/core/baseclasses/BaseEnumeration.py (line:366)


Get enumeration value based on item name as provided to L{registerItem}


printdoc
--------


* params:
* path:/core/baseclasses/BaseEnumeration.py (line:419)


