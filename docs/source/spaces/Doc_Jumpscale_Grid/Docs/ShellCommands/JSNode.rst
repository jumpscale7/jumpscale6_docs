


jsnode
******


use how nodes are attached to grid




.. code-block:: python

  usage: jsnode [-h] [-nid NID] [--roles ROLES]
                {delete,list,enable,disable,addrole,deleterole}
  
  positional arguments:
    {delete,list,enable,disable,addrole,deleterole}
                          Command to perform
  
  optional arguments:
    -h, --help            show this help message and exit
    -nid NID, --nodeid NID
                          ex: -nid=1(note the = sign)
    --roles ROLES         Used with addrole or deleterole. ex: --roles=node,
                          computenode.kvm(note the = sign). List is comma
                          seperated



Deletenode
==========

This command deletes a node from a grid and deletes all its relevant data (ex: logs, jobs, stats... etc)



.. code-block:: python

  jsgrid deletenode -nid=1

If nid is not supplied, the shell command will interactively list all nodes and ask which is to be deleted.



Listnodes
=========

This command lists all nodes in a grid and their properties.



.. code-block:: python

  jsgrid listnodes
  
  #Example output
  NODE ID  NAME        IP ADDRESS                         ACTIVE   ROLES                    
  =============================================================================================
  
  2       testnode 10.0.3.105                             True     computenode.kvm, node



Enablenode and disablenode
==========================



.. code-block:: python

  jsgrid enablenode [-nid=2]
  #OR
  jsgrid disablenode [-nid=2]

If nid is not supplied, the shell command will interactively list all nodes and ask which is to be enabled/disabled.



setrole
=======



.. code-block:: python

  jsgrid setrole [-nid=2] [--roles]


* If nid is not supplied, the shell command will interactively list all nodes and ask which node to set role to
* If roles are not supplied, user will be asked to enter roles


deleterole
==========



.. code-block:: python

  jsgrid deleterole [-nid=2] [--roles]


* If nid is not supplied, the shell command will interactively list all nodes and ask which node to set role to
* If roles are not supplied, current node roles will be interactively listed and user will be asked to choose which to remove.
