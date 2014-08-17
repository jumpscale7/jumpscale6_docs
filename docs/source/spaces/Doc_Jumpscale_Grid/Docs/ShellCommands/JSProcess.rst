

JSProcess
*********

logs
====



.. code-block:: python

  jsprocess logs -d jumpscale -n grid_portal




attach
======



.. code-block:: python

  jsprocess attach -n grid_portal

Will open the tmux window where grid_portal is running



status
======



.. code-block:: python

  jsprocess status
  
  #EXAMPLE OUTPUT
  DOMAIN               NAME                 PRIORITY   STATUS       AUTOSTART  S #  PIDS
  ----------------------------------------------------------------------------------------------------
  
  jumpscale            processmanager       0          HALTED       disabled   S 0  
  jumpscale            redisp               1          RUNNING      enabled      1  567
  jumpscale            redisc               1          RUNNING      enabled      1  563
  jumpscale            redism               1          RUNNING      enabled      1  586
  jumpscale            sentry               1          RUNNING      enabled      1  
  jumpscale            redisac              1          RUNNING      enabled      1  576
  jumpscale            elasticsearch        1          RUNNING      enabled      1  1220
  jumpscale            osis                 15         RUNNING      enabled      1  2081
  jumpscale            agentcontroller      20         RUNNING      enabled      1  2434

Lists all processes managed by processmanager, their domain, their name, priority, status whether they should be autostarted, whether they're a system/js process, number of running processes and their process IDs.



list
====

Same as status



start
=====



.. code-block:: python

  jsprocess start -n grid_portal

start a jsprocess


stop
====



.. code-block:: python

  jsprocess stop -n grid_portal

stop a jsprocess



restart
=======



.. code-block:: python

  jsprocess restart -n grid_portal

restart a jsprocess


disable
=======



.. code-block:: python

  jsprocess disable -n grid_portal

disable a jsprocess


enable
======



.. code-block:: python

  jsprocess enable -n grid_portal

enable a jsprocess
