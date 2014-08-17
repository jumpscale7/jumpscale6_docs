

JPackages Details
*****************


Introduction
============

JumpScale has a built-in packaging system, called JPackages. The JPackage system is an easy package system to create, build, and install an uninstall packages in the Jumpscale framework. Multiple JPackages which logically belong together are grouped in a Domain.


The JPackage components
=======================

JPackages use a particular directory structure to store their information. This directory structure is located in
'$jumpscaledir/var/jpackages/'. Under this directory there are 3 subdirectories

* instance: contains a list of active instances of the JPackages
* files: contains the files of the JPackages
* metadata: contains the metadata of the JPackages


A JPackage consists of 2 components:

* The actual files: these are grouped in a Blob and stored on a Blobstor. Each JPackage consists of two files, a hash file and a archive file (.tgz).The hash file is a list of hash-tags of each file in the JPackage. BlobStor uses this hash for addressing packages. It is stored (only) in the metadata. The hash is the only means to retrieve useful data from the Blobstor. The name of the hash file is the calculated hash of the files in the archive. This means that the hash will only change in case of real file changes.

The archive file contains the files of the JPackage.

* The metadata: contains all the information about a JPackage and is stored under: '$jumpscaledir/var/jpackages/metadata/<domain>/<JPackage name>/<instance>'. It contains the 'coderecipe.cfg' and the hrd files and the actions which can be executed on JPackage.


The Blob in depth
=================

All files necessary for the JPackage are stored under '$jumpscaledir/var/jpackages/files/<domain>/<JPackage name>/<instance>'. It is the intermediate folder for both upload and download of the JPackages.

* domain: the domain to which the JPackage belongs
* package: name of the JPackage, mainly this is identical to the name of the application it comprises
* instance: instance of the JPackage


From there the exact location of the files depend on the platform (Windows, Linux, Ubuntu) they can be used on. Generic means that it the files are platform independent. In case files are only to be used for a specifc platform, you will need to place them in the appropriate directory. Only files in the directory that match the platform type or are more generic will be installed. Lets give an example



.. code-block:: python

  [generic]
  	generic_file.py
  [Ubuntu]
  [Ubuntu 32]
      32_bit_file.py
  [Ubuntu 64]
      64_bit_file.py


If we install an Ubuntu 64 bit server and install the JPackage only the generic_file.py and 64_bit_file.py will be installed on the system when installing the JPackage.

The different domains to dowload packages from can can be configured in '$jumpscaledir/cfg/jpackages/sources.cfg'. The actual files of the Blob are stored locally under '$jumpscaledir/var/jpackages/files/<domain>/<JPackage name>/'


The metadata in depth
=====================

Sources.cfg
-----------


In source.cfg located at '$jumpscaledir/cfg/jpackages/sources.cfg' the JPackage domains are configured.




.. code-block:: python

  template:properties
  [jumpscale]
  metadatafromtgz = 0
  qualitylevel = unstable
  metadatadownload = 
  metadataupload = 
  bitbucketaccount = jumpscale
  bitbucketreponame = jp_jumpscale
  blobstorremote = jpackages_remote
  blobstorlocal = jpackages_local



* The section key: eg. jumpscale is the name of the domain
* metadatafromtgz: indicated wheter we should get the metadta from the metadatadonwload link or from mercurial/bitbucket
* metadataupload: link to get metadata from
* metadataupload: ftp to upload metadata tgz to
* bitbucketaccount: account on bitbucket where the metdata lives
* bitbucketreponame: name of the repository in btibucket used for the metadata
* blobstorremote*: key of the remote blobstore to use for this domain
* blobstorlocal*: key of the local/cache blobstore to use for this domain


These keys point to sections in the blobstor.cfg file under '$jumpscaledir/cfg/jsconfig/blobstor.cfg'



The coderecipe
--------------

The coderecipe (codereciipe.cfg) maps where the files of the JPackage will end up on the system once installed.

An example of a coderecipe:



.. code-block:: python

  #$fileOrDir | $destination | $platform | $type | tagsOrLabels
  #types sitepackages, root, base, etc, tmp,bin
  #tagslabels: e.g. config
  #platform empty means generic
  
  apps/portalexample | apps/portalexample | | base | config
  apps/portalbase | apps/portalbase | | base |
  apps/portalftpgateway | apps/portalftpgateway | | base |
  lib/JumpScale/portal | JumpScale/portal | | sitepackages |




In the above example the files in the JPackage Blob will be copied from apps/portalexample to the base directory of JumpScale ($jumpscaledir) under apps/portalexample.




HRD files
---------



JPacakges consist out of two sets of HRD files one describing the content of the JPacakge itself, intcluding the location where the code of the jpackage lives.
The other one to provider configuration specific to the JPackage eg. port number for a service to run on.


hrd/
^^^^


This folder contains two files main.hrd and code.hrg

'main.hrd'



.. code-block:: python

  template:properties
  jp.domain=jumpscale
  jp.name=core
  jp.version=1.0
  jp.autobuild=0
  
  #supported platforms linux, linux32, linux64, win32, win64, win
  jp.supportedplatforms=generic
  jp.buildnr=199
  
  jp.taskletschecksum=45df7bff22557c2b2f1eafba4581e358
  jp.descrchecksum=400304f8eea1d81743bad25e030c65e3
  jp.hrdchecksum=f371d083055d43f0799804235a179497
  
  jp.bundles=generic:eed95debb2a49fe5c52ea650263615a2,ubuntu64:78dc0845394202b7cfa7e961bb9fb5e4
  jp.dependency.1.name = core
  jp.dependency.1.domain = jumpscale
  jp.dependency.1.minversion=
  jp.dependency.1.maxversion=
  jp.process.tcpports=
  jp.process.startuptime=30



This file describes the content of the JPackage including the location the blobs can be found on the blobstore.
It also points to the required dependencies.




hrdactive/
^^^^^^^^^^


In this folder we store HRD files with configuration settings specific to JPackage for. eg: service port for the JPackage.

'grid.hrg'



.. code-block:: python

  template:properties
  grid.node.roles = @ASK name:roles descr:roles__comma_separated type:str default:node,computenode.kvm
  gridmaster.grid.id=@ASK descr:specify__id__for__this__grid__needs__to__be__unique__globally type:int default:1 minValue:1 maxValue:32767 retry:5
  grid.master.superadminpasswd = rooter


These configuration options can be either asked dynamicly or filled in upfront.
These keys will be merged with the content of '$jumpscaledir/cfg/hrd/*' if a key already exists in this location this value will be used instead of the value from the JPackage als it wont be asked if required.



hrdinstance/
^^^^^^^^^^^^


In this folder we store HRD files with configuration settings specific to a JPackage instance. eg: name of the JPackage instance.

'agent.hrd'



.. code-block:: python

  template:properties
  agent.agentcontroller.ip=@ASK name:ip type:str default:['127.0.0.1']


These configuration options can be either asked dynamicly or filled in upfront.
These keys will be merged with the content of '$jumpscaledir/cfg/hrd/*' if a key already exists in this location this value will be used instead of the value from the JPackage.



Actions
-------

The Actions directory contains all the actions which can be performed or by the JPackage. This ranges from install actions to monitoring actions and even process management of the installed processes by the JPackage.

* The install actions are triggered when the JPackage is installed and are executed in following order: prepare, download, copy, post and configure.
* The monitoring actions are used to install monitoring tasks and retrieve values from the monitored items. You can set up local monitor tasks (monitor.up.local, no network is used) and monitoring tasks to be executed on other nodes ( monitor.up.net.py, the network is used).
* The process actions allow to define the different processes which are to be managed by the JPackage. This allows to start, stop or even kill all the processes required to run the JPackage in an easy fashion.


Files in JPackage
=================



When storing files manually in a JPacakage we need to put them in the correct platform and type folder.

An example folder could be '/opt/jumpscale/var/jpackages/files/<domain>/<packagename>/<instance>/<platform>/<type>/myfile'

The platforms that exist on the system can be retreieve as




.. code-block:: python

  j.system.platformstypes.getPlatforms()




We have a certain set of types which do specific actions with the files stored.
Types are simular to the types defined in the coderecipe section (this is actually where they are stored).
One exception does exists however which is 'debs' when putting any deb file in this folder it will get installed automatically  upon install of the JPackage.






