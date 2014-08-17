

How to install a grid in a modular way
**************************************

components
==========

ProcessManager
--------------


* on each node
* controls local running processes


AgentController = GridMaster
----------------------------


* runs on 1 node
* is the boss of the grid
* requires osis (osis does not need to run on same node)
* all process managers connect to the agentcontroller


OSIS = Object Storage & Indexing Server
---------------------------------------


* requires elasticsearch cluster & keyvalue stor
* the std keyvalue stor is on local filesystem


Graphite if statistics are required
-----------------------------------


* OSIS populates Graphite for statistics of the grid.


GridPortal
----------


* runs on any node & talks to OSIS & the AgentController


Detailed Installation Instructions
==================================


