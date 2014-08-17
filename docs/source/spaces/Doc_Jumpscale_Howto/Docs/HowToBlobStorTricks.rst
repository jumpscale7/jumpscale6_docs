


How to play tricks with blobstor 1
**********************************

example config
==============




.. code-block:: python

  [jpackages_local]
  ftp =
  type = local
  http =
  localpath = /opt/jpackagesftp
  namespace = jpackages
  
  [jpackages_remote]
  ftp = ftp://jpackages:rooter@jpackages.vscalers.com
  #ftp = ftp://iaas:arakoon@publicrepo.incubaid.com
  type = ftp
  localpath =
  namespace = jpackages



run your own blobstor server
============================


see also HowToRunYourOwnBlobStorServer <HowToRunYourOwnBlobStorServer>

this is ideal to use when you play with LXC containers.
You don't want to download everything to a local dir in each container, this allows you to run one locally on the host & each LXC container gets it from there.
When there is a cache miss then the blob gets downloaded from remote into local which is also a local ftp server (blobserver)




.. code-block:: python

  [jpackages_local]
  ftp = ftp://jpackages:rooter@10.10.253.1
  type = ftp
  localpath =
  namespace = jpackages




copy relevant jpackage blobs to a new jpackages blobstor
========================================================


add something like to the blobstorconfig



.. code-block:: python

  [jpackages_new]
  ftp = ftp://jpackages:rooter@localhost
  type = ftp
  localpath =
  namespace = jpackages


now use the following command



.. code-block:: python

  jpackage upload --blobserver=jpackages_new --onlyexistingblobs -d jumpscale


example for domain: jumpscale

this will download all jpackages from local or remote store & then upload to the jpackages_new


