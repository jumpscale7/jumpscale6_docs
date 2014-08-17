

Installing the Portal
=====================

The JumpScale portal requires the JumpScale framework to be installed. So if you didn't do so install JumpScale <UbuntuManual>.



.. code-block:: python

  apt-get update
  apt-get install mercurial ssh python2.7 python-apt openssl ca-certificates python-pip ipython -y
  pip install https://bitbucket.org/jumpscale/jumpscale_core/get/unstable.zip
  jpackage mdupdate
  jpackage install -n core


In the above code we installed the unstable version. Replace unstable.zip by default.zip to install the latest stable version.

After installing the JumpScale framework, you can install the portal.



.. code-block:: python

  jpackage install -n portal


During the install you will need to enter a a name for the Elasticsearch application and an encryption key for the OSIS database.

Start the portal by starting the necessary processes:



.. code-block:: python

  jsprocess start


This completes the steps to install the JumpScale portal. Now you can create a new portal <How to get started> or import an existing project from BitBucket. In the below example we will make the JumpScale Documentation portal in our newly installed poral.

Edit $jumpscaledir/cfg/jpackages/sources.cfg and add the Incubaid domain.



.. code-block:: python

  [incubaid]
  metadatafromtgz = 0
  qualitylevel = unstable
  metadatadownload = 
  metadataupload = 
  bitbucketaccount = incubaid
  bitbucketreponame = jp_incubaid
  blobstorremote = jpackages_remote
  blobstorlocal = jpackages_local


Update the metadata and install and start the Incubaid portals.



.. code-block:: python

  jpackage mdupdate
  jpackage install -n  portals_base
  jpackage start -n portals_base

When asked provide a free port on your host to serve the webpages. You can now see browse to the portal on http://<your IP address>:<port>

Next download the documentation package



.. code-block:: python

  jpackage install -n doc_jumpscale


