



.. code-block:: python

  WARNING:
  we need to improve the documentation on this page




Generic Spec Format:
********************

at beginning of line (can be intended):

method:$nameofmethod $optionalDescriptionOfMethod
var:$nameofvar $type,$defaultval,$description
return:$type $description


basic types
===========


see Types </doc_jumpscale_grid/types>


reference to enumerations & objects
===================================


machinemanager.machine  #this means a model object of actor machinemanager with name machine, no needed to specify actor, tool will look for it
machinemanager.machine.status #means enumeration of type machine.status of actor machinemanager (tool will figure out if enumeration or model object)


default val posibilities
========================


"forstring"
44 #is a nr
True & False
None
can also use the name of a model object e.g. machinemanager.machine will then create an empty object

any valid python statement will do but then need to be surrounded by %%

this is used for lists & dicts

* [] #python format for a list
* {} #python format for a dict


for %...% the interpretion will be done by means of python eval (so it should be valid python statement)

if nothing specified then there is no default value


Generic
=======


"""
description of element defined above
"""



