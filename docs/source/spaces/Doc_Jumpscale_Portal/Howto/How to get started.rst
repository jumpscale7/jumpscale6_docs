

Quick Start
===========




To make your own portal
^^^^^^^^^^^^^^^^^^^^^^^


*(Replace <appname> with your own appname)*


Create folder @ *$jumpscaledir/apps/<appname>*. You'll also need to create a cfg folder within your app




.. code-block:: python

  mkdir -p $jumpscaledir/apps/<appname>/cfg/



Create config @ *$jumpscaledir/apps/<appname>/cfg/appserver.cfg*




.. code-block:: python

  [main]
  appdir = $jumpscaledir/apps/portalbase
  dbtype=fs
  filesroot = $vardir/filesroot
  wwwroot = www
  
  [process_1]
  actors = *
  secret = 1234
  webserverport = 9999
  ismaster = 1



Create a script to start your application @ *$jumpscaledir/app/<appname>/start_appserver.py*




.. code-block:: python

  from JumpScale import j
  j.application.start('myapp')
  
  import JumpScale.portal #load portal libraries
  j.manage.portal.startprocess()
  j.application.stop()



To start the application server run in **terminal**:



.. code-block:: python

  python start_appserver.py

