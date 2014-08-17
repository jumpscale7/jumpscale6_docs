
watchdog
********

server = watchdog manager
=========================


to install



.. code-block:: python

  jpackage configure -n grid_node
  jpackage install -n webdis
  jpackage install -n watchdogmanager



to use client
=============


this will make sure the following HRD params are added:



.. code-block:: python

  grid.watchdog.secret=
  grid.watchdog.addr=


make sure they are filled in properly where you want to use watchdog functionality
secret is a long key, providing security for your grid
the secret needs to be the same for the FULL grid.

the addr is a comma separated list for addr to use to send watchdogs too





.. code-block:: python

  import JumpScale.baselib.watchdogclient
  j.tools.watchdogclient.send("cpu.core","OK",90)



types of watchdogs
==================





