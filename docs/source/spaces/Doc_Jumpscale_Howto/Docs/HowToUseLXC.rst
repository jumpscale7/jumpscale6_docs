

How to use LXC
**************

Intro
=====


jsmachine
=========


is the main tool to interact with lxc




.. code-block:: python

  # jsmachine --help
  usage: jsmachine [-h] [-n NAME] [-m BNAME] [-b BASE] [-p PASSWD] [-r PREFIX]
                   [-k KEY] [-c CMD] [-a PUBIP] [-g GW] [--start]
                   
                   {ps,new,list,destroyall,destroy,cmd,rdp,ssh,start,stop,restart,getip,exportTGZ,importTGZ,exportR,importR}
  
  positional arguments:
    {ps,new,list,destroyall,destroy,cmd,rdp,ssh,start,stop,restart,getip,exportTGZ,importTGZ,exportR,importR}
                          Command to perform
  
  optional arguments:
    -h, --help            show this help message and exit
    -n NAME, --name NAME  machine name
    -m BNAME, --bname BNAME
                          name of backup (used for import/export)
    -b BASE, --base BASE  base to clone from
    -p PASSWD, --passwd PASSWD
                          password for machine
    -r PREFIX, --prefix PREFIX
                          prefix
    -k KEY, --key KEY     key for syncing
    -c CMD, --cmd CMD     cmd to execute
    -a PUBIP, --pubip PUBIP
                          set pub ip addr of machine (192.168.1.207/24)
    -g GW, --gw GW        set ip gateway of machine (192.168.1.1)
    --start               start after creation



create your first machine
=========================


create a machine to start working with



.. code-block:: python

  jsmachine new -n test -b base -a 192.168.1.31/24 -g 192.168.1.1 --start


-a 192.168.1.31 is from existing range on my network
-g is the gateway
make sure the netmask is properly done

the --start will try to ssh the just created lxc


list machines
=============




.. code-block:: python

  # jsmachine list
  ## running:
    machine: test                      10.10.253.4
  ## stopped:
    machine: base                      10.10.253.7
    machine: sentry                    10.10.253.3



remote execute something on machine(s)
======================================




.. code-block:: python

  jsexec -r test -x "ls /" -s


-s will do it synchronously




.. code-block:: python

  jsexec -r test,test3 -x "ls /"


will execute both in parallel & show result



