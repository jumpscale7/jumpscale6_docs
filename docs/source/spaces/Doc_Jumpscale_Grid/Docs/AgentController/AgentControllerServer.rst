

Agentcontroller
***************


Description.
============


The Agentcontroller is repsonsible of distrubuting the work over the nodes.
This can be accomplished by specifying a specific node id to execute on or based on a role.


Roles.
======


Each node can provided a role.
Roles define what each node is capable of doing.


Executing of a task (JumpScript)
================================


In JumpScale one can define a task in a JumpScript <JumpScript>
As JumpScript <JumpScript> defines a set of intruction to execute how and where to do so.



Agentcontroller client
======================

ExcecuteJumpScript
------------------


In the JSShell one can execute a task as followed




.. code-block:: python

  import JumpScale.grid.agentcontroller
  acl = j.clients.agentcontroller.get()
  job = acl.executeJumpScript(organization='jumpscale', name='jumpscale', nid=1, role=None, args={'msg':'bleh'}, timeout=600, wait=True, queue='')
  print job['result']



Paramters Explained
^^^^^^^^^^^^^^^^^^^


* organization: is the organization the JumpScript is written by
* name: the name of the jumpscript
* nid: This is the node id of the node that should execute is (can be overruled by role)
* role: If role is specified it will be used instead of nid, the agentcontroller will search for a node which specifies this role and execute it on this node. If multiple nodes match a role the first available will be chosen.
* args: This is a dictionary of arguments to give to the JumpScript
* wait: When we want to perform a task either async or sync we can choose to wait for the result when providing False this method will return a Job object which is either queued or in progress.
* queue: With the parameter queue one can specify on which worker to execute his/her task.


remarks
^^^^^^^


when more than 1 node matches the role then only the first matching one will be used


ListSessions
------------


This method provides an insight on which nodes are connected to the AgentController.
It provides which nodes is connected with which roles.




.. code-block:: python

  import JumpScale.grid.agentcontroller
  acl = j.clients.agentcontroller.get()
  sessions = acl.listSessions()



