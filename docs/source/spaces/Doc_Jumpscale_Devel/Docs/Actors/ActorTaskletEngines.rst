



.. code-block:: python

  WARNING:
  we need to improve the documentation on this page




Actors Tasklets Engines
***********************


this is advanced functionality only useful in very specific usecases.

create subdir 'taskletengines' under actor path
each subdir under 'taskletengines' will be used as a key to link the tasklet engine to the actor object

e.g.
$actorobjectpath/taskletengines/processevents/$1_tasklet.py ...

will be linked to:
actorobject.taskletengines.processevents

will be a tasklet engine linked to that dir

ideal for e.g. event mgmt, log mgmt, ...




