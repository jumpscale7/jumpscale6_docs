

Process Management In Jumpscale
*******************************

jsprocess
=========


is the main command to manage processes in a jumpscale environment.


jsprocess list
==============


lists all known processes
when disabled will not start automatically
priority is priority of starting





.. code-block:: python

  # jsprocess list
  DOMAIN               NAME                 PRIORITY   STATUS       AUTOSTART  S #  PIDS
  ----------------------------------------------------------------------------------------------------
  
  jumpscale            redisac              1          RUNNING      enabled      1  
  jumpscale            redism               1          RUNNING      enabled      1  
  jumpscale            elasticsearch        1          RUNNING      enabled      1  
  jumpscale            redisp               1          RUNNING      enabled      1  
  jumpscale            redisc               1          RUNNING      enabled      1



jsprocess disable
=================




.. code-block:: python

  jsprocess disable -n portals_base


disables a specific process and also stops it if still running



jsprocess cmd
=============




.. code-block:: python

  usage: jsprocess [-h] [-n NAME] [-d DOMAIN] [-c]
                   {logs,attach,list,status,start,stop,restart,disable,enable}
  
  positional arguments:
    {logs,attach,list,status,start,stop,restart,disable,enable}
                          Command to perform
  
  optional arguments:
    -h, --help            show this help message and exit
    -n NAME, --name NAME  Process name
    -d DOMAIN, --domain DOMAIN
                          Process domain
    -c, --carefull        Check each startup status, die if one could not start.



