

jsexec
******




.. code-block:: python

  # jsexec --help
  usage: jsexec [-h] [-r REMOTE] [-p PASSWD] [-n NAME] [-o GRIDNAME]
                [-c CFGNAME] [-e EXTRA] [-f] [-x COMMAND] [-s] [-g]
                [--roles ROLES] [-t TIMEOUT] [--runid RUNID] [--reset]
  
  optional arguments:
    -h, --help            show this help message and exit
    -r REMOTE, --remote REMOTE
                          hostname of node.
    -p PASSWD, --passwd PASSWD
                          Root password to use, if any.
    -n NAME, --name NAME  Names of jumpscript to execute (comma separated)
    -o GRIDNAME, --gridname GRIDNAME
                          Name of grid.
    -c CFGNAME, --cfgname CFGNAME
                          Name of cfg directory.
    -e EXTRA, --extra EXTRA
                          Extra config data in tag format e.g.
                          cpasswd:123,myname:kds
    -f, --force           auto answer yes on every question and redo even if
                          already done
    -x COMMAND, --command COMMAND
                          if this one is used then just this command will be
                          execute
    -s, --sync            then will be done one after the other
    -g                    Apply on all active nodes on grid
    --roles ROLES         Used with -g. Apply on active nodes that have these
                          roles. ex: --roles=node, computenode.kvm(note the =
                          sign). List is comma seperated
    -t TIMEOUT, --timeout TIMEOUT
                          Time to wait to if connection is not available
    --runid RUNID         Give run a specific id.
    --reset               If reset info for that run will be removed from redis.





usage of runid
==============


* when launching a run if you specify a runid, then jsexec will remember which nodes where already executed ok and will not be repeated
* if jsexec hangs or crashes (in async mode can happen) you can always look at result by doing 'jsadmin print --runid=$yourrunid'


selection criteria are much more flexible as before
===================================================


* see AdminPrinciples <AdminPrinciples>


sync or not to sync
===================


* make sure you run it with --runid=$yourRunId
* when many nodes, best is to start sync to see script is running
* if ok then stop jsadmin and then run async
* now it will go much faster, let it finish
* you will see all the ones which did not succeed yet, run again but now sync and repair issue by issue


some examples
=============

