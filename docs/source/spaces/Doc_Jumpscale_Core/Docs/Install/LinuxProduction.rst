

This Explains how to manually install JumpScale in sandboxed mode
=================================================================


Tested on 13.10 & 14.04 64 bit.
does also work on equavelant mint distro 64 bit.

update your apt repository & make sure some basic requirements are met



.. code-block:: python

  template:shell
  apt-get update
  #apt-get upgrade
  apt-get install mercurial ssh mc curl -y




to make sure you remove previous version od
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^




.. code-block:: python

  pip uninstall JumpScale-core


if you are not sure please do



.. code-block:: python

  killall tmux
  rm -rf /usr/local/lib/python2.7/dist-packages/jumpscale*
  rm -rf /usr/local/lib/python2.7/site-packages/jumpscale*
  rm -rf /usr/local/lib/python2.7/dist-packages/JumpScale*
  rm -rf /usr/local/lib/python2.7/site-packages/JumpScale*
  rm -rf /usr/local/lib/python2.7/site-packages/JumpScale/
  rm -rf /usr/local/lib/python2.7/site-packages/jumpscale/
  rm -rf /usr/local/lib/python2.7/dist-packages/JumpScale/
  rm -rf /usr/local/lib/python2.7/dist-packages/jumpscale/
  rm -rf /opt/jumpscale
  rm /usr/local/bin/js*
  rm /usr/local/bin/jpack*
  killall python
  rm -rf /opt/sentry/
  killall redis-server
  rm -rf /opt/redis/
  apt-get update
  apt-get upgrade

this will make sure all leftovers are gone


Install the sandbox
^^^^^^^^^^^^^^^^^^^




.. code-block:: python

  template:shell
  curl http://install.jumpscale.org:85/cmds/jsbox_stable.sh > /tmp/init.sh;sh /tmp/init.sh
  source /opt/jsbox/activate
  js




Update the jpackage metadata
^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Run the following command:




.. code-block:: python

  template:shell
  jssync download -c jpackages -k test
  #or for stable
  jssync download -c jpackages -k unstable




install jumpscale documentation in a development env which is also master
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

just do



.. code-block:: python

  jpackage install -n redis
  jpackage install -n grid_master_singlenode
  #creates user admin with passwd admin for grid_portal
  jsuser add -d admin:admin:admin:ikk@com:jumpscale 
  #visit localhost:81 to see gridportal
  jpackage install -n doc_jumpscale


this will install all components required to work with the documentation from a local portal.
This will also install osis, elasticsearch, processmanager, redis



