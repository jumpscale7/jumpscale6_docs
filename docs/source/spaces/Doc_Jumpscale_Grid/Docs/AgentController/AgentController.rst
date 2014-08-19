
Distributed Work Controller
***************************

Introduction.
=============


JumpScale provides the capability to execute tasks over the grid.
Those tasks can be executed in the following manners.

* async, task is executed in a worker <workers>
* sync, task is executed in the processmanager <processmanager>
* on interval, task is executed either in the processmanager <processmanager> or worker <workers> on the specified interval


Components
==========


* Agentcontroller <Agentcontroller>
* ProcessManager <ProcessManager>
* Worker <Worker>


How To
======


* Schedule work using agentcontroller <ScheduleWork>
