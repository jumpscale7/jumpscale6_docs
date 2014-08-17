
Processmanager
**************

Description
===========


The processmanager has multiple purposes. It acts as an agent towards the AgentController it makes connections to it and asks for tasks. It schedules JumpScript by interval and keeps track of processes.

When the ProcessManager receives a task from the AgentController it validates if it should be execute sync or async or on which queue. When it should be execute async it executes it itself. When the job however has a queue or is requested to be execute async it is put on the correct queue, when the queue is empty and async is true the default queue is used.


how to debug a process manager
==============================




.. code-block:: python

  jsprocess disable -n processmanager


open a new console
and do:



.. code-block:: python

  cd /opt/jumpscale/apps/processmanager/
  python processmanager.py


you will now see the output from the process manager

to check e.g. that processmanager reloads do




.. code-block:: python

  jsgrid restartprocessmgrs


