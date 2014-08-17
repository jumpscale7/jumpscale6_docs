

jsadmin
*******




.. code-block:: python

  # jsadmin --help
  usage: jsadmin [-h] [--runid RUNID] [-r REMOTE] [-o GRIDNAME]
                 
                 {applyconfiglocal,createidentity,config2gridmaster,sshfs,sshfsoff,listnodes,kill,print}
  
  positional arguments:
    {applyconfiglocal,createidentity,config2gridmaster,sshfs,sshfsoff,listnodes,kill,print}
                          Command to perform
  
  optional arguments:
    -h, --help            show this help message and exit
  
  all:
    --runid RUNID         Give run a specific id.
  
  sshfs:
    -r REMOTE, --remote REMOTE
                          hostname of node.
    -o GRIDNAME, --gridname GRIDNAME
                          Name of grid.




applyconfig
===========


* no arguments
* will write local hostfile as follows

  * $hostname.$gridnameLong
  * $hostname.$gridnameAlias
  * all in lowercase


e.g. ping cpu01.l1 pings cpu01 of lenoir1  (cpu.lenoir1 would give same result)


remarks
-------

* the existing names in hostfile will be remembered
* the names generated will be put behind ###################
* make sure you put your custom names in hosts file before ######################


sshfs & sshfsoff
================

sshfs
-----




.. code-block:: python

  jsadmin sshfs -r cpu01 -o lenoir1


make sshfs connection to cpunode 1 on lenoir 1
will get mounted under:

* jsbox -> /mnt/$gridname_$nodename_jsbox
* jsbox_data -> /mnt/$gridname_$nodename_jsbox_data


jsadmin sshfsoff
----------------


* will remove all existing sshfs connections
* if files are occupied jsadmin will try to find which tools occupy the mount & warn about it


jsadmin listnodes
=================


* prints a formatted list of all nodes known to jsadmin


jsadmin createidentity
======================


* use this to create your personal info & ssh keys
* copy the private key to your secure spot
* these identities are used to give people access to environments


jsadmin print --runid=update
============================


* with jscript a runid can be specified, a runid is a specific name which is given to a jsexec run e.g. update all nodes in a specific grid
* with jsadmin -port -runid=update the result info from the run is printed, can be usefull when e,g, jsexec stopped and later you want tosee the result

*




.. code-block:: python

  jsadmin sshfs -r admin -o lenoir2


exception is node admin (on an admin node jumpscale should be in debug mode)

* /opt/code -> /mnt/$gridname_$nodename_code
* /opt/jumpscale -> /mnt/$gridname_$nodename_jumpscale


jsadmin kill
============


* kills all remaining jsexec & jsadmin processes, this to cleanup from a messed up state


jsadmin config2gridmaster
=========================


* read all node & jumpscript info and send it over webdis to the gridmaster
* on the gridmaster this info can be looked at
* you can see on portal on following locations

  * //localhost:81/grid/adminnodes <http://localhost:81/grid/adminnodes>
  * //localhost:81/grid/adminnode?gridname=york1&name=gm1 <http://localhost:81/grid/adminnode?gridname=york1&name=gm1>
  * //localhost:81/grid/adminjumpscripts <http://localhost:81/grid/adminjumpscripts>








