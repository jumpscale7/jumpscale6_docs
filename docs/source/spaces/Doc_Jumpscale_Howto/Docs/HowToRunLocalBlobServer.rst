

Using Local BlobStor
====================


Install jpackage server



.. code-block:: python

  jpackage_install -n jpackageserver
  jpackage_start -n jpackageserver


change on all nodes the
$jumpscaledir/cfg/jsconfig/blobstor.cfg




.. code-block:: python

  #[jpackages_local]
  #ftp =
  #type = local
  #http =
  #localpath = /opt/jpackagesftp
  #namespace = jpackages
  
  #localftp server
  [jpackages_local]
  ftp = ftp://jpackages:rooter@192.168.1.6
  type = ftp
  http = 
  localpath =
  namespace = jpackages
  
  [jpackages_remote]
  ftp = ftp://username:password@publicrepo.incubaid.com
  type = httpftp
  http = http://publicrepo.incubaid.com
  localpath =
  namespace = jpackages


change the ip address ofcourse


