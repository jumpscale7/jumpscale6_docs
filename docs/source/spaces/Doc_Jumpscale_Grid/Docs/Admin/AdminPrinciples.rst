

Admin Principles
****************

Selection of Nodes
==================

-r
--


* specify the hostname
* if -o (specifies the grid) is not used then the active grid will be used, the active grid is the first grid which is encountered in file:///opt/jumpscale/cfg/admin/active.cfg

  * the first one marked with *... (reading from top down)




.. code-block:: python

  * Lenoir2
  cpu01
  cpu02
  * York1
  cpu01


examples:

* -r cpu01 : the cpu01 node from lenoir2 is selected
* -r cpu01 -o york1 : cpu01 from york is selected
* -r cpu03 : cpu03 from Lenoir2 is selected (if cpu03 does not exist in Lenoir2 then error)


-r and -o are used
------------------


* specifies the gridname & nodename
* if combination not found -> error


only -o is used
---------------


* all nodes from file:///opt/jumpscale/cfg/admin/active.cfg above ### (the active nodes) are chosen from appriopriate grid, if none: Error


no o and no  r is used
----------------------


* illegal, error


no o and no  r is used but --roles is specified
-----------------------------------------------


* the nodes with the appropriate roles are looked for over all grids


o and -roles are specified
--------------------------


* the nodes with the appropriate roles are looked for for the specified grid, if not found -> error


g and -roles are specified
--------------------------


* consult the OSIS grid database get the hostnames from there using the roles
* only works against the locally configured grid osis DB (so not over grids)





