

JPackages Tutorial
******************

Introduction
============

This tutorial will walk you through creating a JPackage from scratch, until having it installed. Note that you need to have JumpScale core (at least) to be installed to be able to complete this tutorial.


Create
======

We are going to create a new JPackage, named "example_package", under domain "test" (domain and blobstore configuration will come later). Run the following command from within shell:




.. code-block:: python

  template:shell
  jpackage create


In this tutorial, we will be using *jpackage* commands (Note that all commands functionality are also available through JumpScale jpackages APIs, available under *j.packages*)
The last command, *jpackage create* will trigger a wizard to collect some information about the package you wanna create as follows:




.. code-block:: python

  template:shell
  
   Please select a domain
     1: cloudscalers
     2: jumpscale
     3: test
  
     Select Nr (1-3): 3
  Please provide a name: example_package
  Please provide a version [1.0]: 
  Please provide a description: 
  Please enumerate the supported platforms
     1: cygwin
     2: generic
     3: linux
     4: linux32
     5: linux64
     6: mint
     7: mint32
     8: mint64
     9: ubuntu
     10: ubuntu32
     11: ubuntu64
     12: unix
     13: unknown
     14: vista
     15: win
     16: win2008_64
     17: win2012_64
     18: win32
     19: win64
     20: win7
     21: win8
  
     Select Nr, use comma separation if more e.g. "1,4", * is all, 0 is None: 2
  jpackage_save             :: JPackage test example_package 1.0:saving jpackages data to $jumpscaledir/var/jpackages/metadata/test/example_package/1.0



You need to provide the following information: package domain, name, instance, description and supported platforms.
Now you will have metadata for your package created under *$jumpscaledir/var/jpackages/metadata/<domain>/<package_name>/<instance>*. You can now edit metadata scripts, like *install.prepare.py*, *install.configure.py*, etc for the logic you would like to have it implemented in your package.


Define recipe
^^^^^^^^^^^^^

After creating a new package, you may now need to define a recipe. A code recipe is basically some config files which tell jpackage system which code files your package needs to download to be installed. These files are as follows:

1. *code.hrd*: under *<package_name>/<instance>/hrd/* where you can define your recipe source repo information




.. code-block:: python

  template:properties
  
  jp.code.account=jumpscale
  jp.code.repo=jumpscale_lib
  jp.code.type=bitbucket
  jp.code.branch=



2. *coderecipe.cfg*: under *<package_name>/<instance>/* where you can define the destination for your recipe source files. File format is as follows:





.. code-block:: python

  template:properties
  
  #$fileOrDir | $destination | $platform | $type | tagsOrLabels
  #types sitepackages, root, base, etc, tmp, bin
  #tagslabels: e.g. config
  #platform empty means generic


For example:




.. code-block:: python

  JumpScale/lib | | | tmp |


This will copy *JumpScale/lib* directory under */tmp*.





.. code-block:: python

  apps/osis/tests/ | | | base |


This will copy *apps/osis/tests/* from *jumpscale_grid* repo to *apps/osis/tests/* under *$jumpscaledir* directory on the destination system (this is what *base* means).

*root* means to copy files under root of the file system, *sitepackages* means under */usr/local/lib/python2.7/site-packages* and so on. Platform also can be specified.

After editing metadata scripts, you are ready now to package your jpackage via the following command:




.. code-block:: python

  template:shell
  jpackage package -n 'example_package'


This command will do the following:

1. Execute the package recipe (i.e: check out the recipe files) and copy them under *$jumpscaledir/var/jpackages/files/<domain>/<package_name>/<instance>/<platform>*

2. Create *<platform>___cr_<type>.info* file under *<package_name>/<instance>/files* which contains all the the package's files paths and their MD5 checksum (for each file)

3. Update the build number

After packaging your jpackage, you are ready now to upload your package files to the blobstore. If your package requires any additional files for its installation, you should put them now under *$jumpscaledir/var/jpackages/files/<domain>/<package_name>/* so that they can get uploaded to the blobstore. You also need to have a valid *$jumpscaledir/cfg/jsconfig/blobstor.cfg* file, for example:




.. code-block:: python

  template:properties
  
  [jpackages_local]
  ftp =
  type = local
  http =
  localpath = /opt/jpackagesftp
  namespace = jpackages
  
  [jpackages_remote]
  ftp = ftp://<username>:<password>@publicrepo.incubaid.com
  type = httpftp
  http = http://publicrepo.incubaid.com
  localpath = 
  namespace = jpackages


and also a valid *$jumpscaledir/cfg/jpackages/sources.cfg* file which has a reference to the correct blobstore, for example:




.. code-block:: python

  template:properties
  [test]
  metadatafromtgz = 0
  qualitylevel = unstable
  metadatadownload = 
  metadataupload = 
  bitbucketaccount = jumpscale
  bitbucketreponame = jp_test
  blobstorremote = jpackages_remote
  blobstorlocal = jpackages_local


Note *blobstorremote = jpackages_remote* the same name as in the *blobstor.cfg* for proper files uploading.
Now, if you have these configuration values set correctly, you are ready to call the upload command:




.. code-block:: python

  template:shell
  jpackage upload -n 'example_package'


Now, you should find your package files on the remote blobstore


Publish
^^^^^^^

Now, your jpackage metadata needs to be published to the domain's repo (as specified in the *sources.cfg* file, *bitbucketreponame* field). In order to do this, you will need to call the publish command:




.. code-block:: python

  template:shell
  jpackage publish -n 'example_package'



This command will start a wizard to publish your metadata (i.e: push metadata to their corresponding repo)




.. code-block:: python

  bitbucket_getclient       :: try to init mercurial client:jp_test on path:/opt/code/jumpscale/jp_test
  bitbucket_getclient       :: mercurial client inited for repo:jp_test
  bitbucket_getclient       :: try to init mercurial client:jp_test on path:/opt/code/jumpscale/jp_test
  bitbucket_getclient       :: mercurial client inited for repo:jp_test
  bitbucket_getclient       :: try to init mercurial client:jp_test on path:/opt/code/jumpscale/jp_test
  bitbucket_getclient       :: mercurial client inited for repo:jp_test
  bitbucket_getclient       :: try to init mercurial client:jp_test on path:/opt/code/jumpscale/jp_test
  bitbucket_getclient       :: mercurial client inited for repo:jp_test
  continue? (y/n):y
  please enter a commit message: test
  bitbucket_getclient       :: try to init mercurial client:jp_test on path:/opt/code/jumpscale/jp_test
  bitbucket_getclient       :: mercurial client inited for repo:jp_test
  bitbucket_getclient       :: try to init mercurial client:jp_test on path:/opt/code/jumpscale/jp_test
  bitbucket_getclient       :: mercurial client inited for repo:jp_test
  jpackage_save             :: JPackage test example_package 1.0:saving jpackages data to $jumpscaledir/var/jpackages/metadata/test/example_package/1.0
   * updatejpackages metadata for domain testbitbucket_getclient       :: try to init mercurial client:jp_test on path:/opt/code/jumpscale/jp_test
  bitbucket_getclient       :: mercurial client inited for repo:jp_test
  * pull jp_test
  Found files not added yet to repo or deleted from filesystem
  Nottracked/Ignored: unstable/example_package/1.0/actions/code.commit.py
  Nottracked/Ignored: unstable/example_package/1.0/actions/code.export.py
  Nottracked/Ignored: unstable/example_package/1.0/actions/code.link.py
  Nottracked/Ignored: unstable/example_package/1.0/actions/code.package.py
  Nottracked/Ignored: unstable/example_package/1.0/actions/code.push.py
  Nottracked/Ignored: unstable/example_package/1.0/actions/code.update.py
  Nottracked/Ignored: unstable/example_package/1.0/actions/data.export.py
  Nottracked/Ignored: unstable/example_package/1.0/actions/data.import.py
  Nottracked/Ignored: unstable/example_package/1.0/actions/data.logrotate.py
  Nottracked/Ignored: unstable/example_package/1.0/actions/install.configure.py
  Nottracked/Ignored: unstable/example_package/1.0/actions/install.copy.py
  Nottracked/Ignored: unstable/example_package/1.0/actions/install.download.py
  Nottracked/Ignored: unstable/example_package/1.0/actions/install.post.py
  Nottracked/Ignored: unstable/example_package/1.0/actions/install.prepare.py
  Nottracked/Ignored: unstable/example_package/1.0/actions/monitor.getstats.py
  Nottracked/Ignored: unstable/example_package/1.0/actions/monitor.up.local.py
  Nottracked/Ignored: unstable/example_package/1.0/actions/monitor.up.net.py
  Nottracked/Ignored: unstable/example_package/1.0/actions/process.configure.py
  Nottracked/Ignored: unstable/example_package/1.0/actions/process.depcheck.py
  Nottracked/Ignored: unstable/example_package/1.0/actions/process.kill.py
  Nottracked/Ignored: unstable/example_package/1.0/actions/process.start.py
  Nottracked/Ignored: unstable/example_package/1.0/actions/process.stop.py
  Nottracked/Ignored: unstable/example_package/1.0/actions/process.unconfigure.py
  Nottracked/Ignored: unstable/example_package/1.0/actions/uninstall.py
  Nottracked/Ignored: unstable/example_package/1.0/actions/upload.py
  Nottracked/Ignored: unstable/example_package/1.0/coderecipe.cfg
  Nottracked/Ignored: unstable/example_package/1.0/description.wiki
  Nottracked/Ignored: unstable/example_package/1.0/documentation/main.wiki
  Nottracked/Ignored: unstable/example_package/1.0/files/generic___cr_tmp.info
  Nottracked/Ignored: unstable/example_package/1.0/hrd/code.hrd
  Nottracked/Ignored: unstable/example_package/1.0/hrd/main.hrd
  Nottracked/Ignored: unstable/example_package/1.0/hrdactive/_example.hrd
  Nottracked/Ignored: unstable/example_package/1.0/hrdactive/readme.txt
  Nottracked/Ignored: unstable/example_package/1.0/releasenotes.wiki
  Nottracked/Ignored: unstable/example_package/1.0/uploadhistory/generic___cr_tmp.info
  \Above files are not added yet to repo but on filesystem
  What do you want to do with these files
     1: Abort
     2: AddRemove
     3: RemoveTheseFiles
  
     Select Nr (1-3): 2
                    DONE
  bitbucket_getclient       :: try to init mercurial client:jp_test on path:/opt/code/jumpscale/jp_test
  bitbucket_getclient       :: mercurial client inited for repo:jp_test
  * commit push jp_test



Install
^^^^^^^

Now, your jpackage example_package is successfully created, published and ready to be consumed via any JumpScale system which of course has the required configuration for the package to be installed (i.e: *sources.cfg*, *blobstor.cfg*)
In order to install your jpackage, run the install command:




.. code-block:: python

  template:shell
  jpackage install -n 'example_package'


Note:
There is a command *jpackage repackage* which can do the package, upload and publish for you. Check the JPackages Commands <JPackagesCommands> page for other available jpackages commands




Using JPackage instances
========================
You can install the same package in different instances.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For example, instead of only one agent, you want to have more.
'jpacakge install -n agent -i test'
This will install a new agent instance called "test"

You could also have different configurations for different instances, by configuring an hrd under "hrdinstance" of the jpackage
Example:



.. code-block:: python

  agent.agentcontroller.ip=@ASK
  agent.agentcontroller.secret=@ASK


this will enable different configs for different instances of the same jpackage
