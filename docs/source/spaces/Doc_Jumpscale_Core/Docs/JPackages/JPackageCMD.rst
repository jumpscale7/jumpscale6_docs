

jpackage command
****************


is the tool to manipulate jpackages on your system




.. code-block:: python

  template:shell
  # jpackage --help
  usage: jpackage [-h] [-q] [-n NAME] [-d DOMAIN] [-i INSTANCE] [-v VERSION]
                  [--deps] [-f] [--data DATA] [-r] [-s] [--debug] [--nodownload]
                  [--installed] [--enable | --disable] [--injpackage] [--list]
                  [--nocode] [--noexpand] [--copy] [-m MESSAGE] [-l] [-p]
                  [--merge] [--onlycode] [--onlyexistingblobs]
                  [--blobserver BLOBSERVER] [--branch BRANCH]
                  [--qualitylevel QUALITYLEVEL] [-ql QL] [-bba BBA] [-bbr BBR]
                  
                  {create,configure,debug,download,export,install,link,monitor,package,publish,repackage,restart,start,stop,mdupdate,addrepo,update,upload,mirror,switchbranch,list,mdswitch,mddisabledebug}
  
  positional arguments:
    {create,configure,debug,download,export,install,link,monitor,package,publish,repackage,restart,start,stop,mdupdate,addrepo,update,upload,mirror,switchbranch,list,mdswitch,mddisabledebug}
                          Command to perform
  
  optional arguments:
    -h, --help            show this help message and exit
  
  Package Selection:
    -q, --quiet           Put in quiet mode
    -n NAME, --name NAME  Name of jpackage to be installed
    -d DOMAIN, --domain DOMAIN
                          Name of jpackage domain to be installed
    -i INSTANCE, --instance INSTANCE
                          Instance of jpackage (default 0)
    -v VERSION, --version VERSION
                          Version of jpackage to be installed
    --deps                do on dependencies e.g. install, update, ...
    -f, --force           auto answer yes on every question
  
  Install/Update/Expand/Configure:
    --data DATA           use this to pass hrd information to jpackage e.g.
                          'redis.name:system redis.port:7766 redis.disk:0'
    -r, --reinstall       Reinstall found package
    -s, --single          Do not install dependencies
    --debug               Sets debug_mode for package
    --nodownload          skips download
  
  List:
    --installed           List installed jpackages
  
  Debug:
    --enable
    --disable
    --injpackage          if set then will set jpackage in debug mode on repo,
                          so will count for all.
    --list
  
  Download:
    --nocode              do not download the files which were build using the
                          coderecipe
    --noexpand            do not expand locally
    --copy                copy downloaded files to local fs
  
  Repackage / Publish:
    -m MESSAGE, --message MESSAGE
                          Commit message to publish package
    -l, --local           Only repackage locally
    -p, --publish         Publish metadata
    --merge               Merge existing content of jpackage files with recipe
                          if ommited clean existing content.
  
  Upload:
    --onlycode            to only upload jpackage files which are for
                          coderecipes
    --onlyexistingblobs   to only upload jpackage blobs which do exist in one of
                          existing blobstores
    --blobserver BLOBSERVER
                          only upload to specified blobserver
  
  Switch Branch:
    --branch BRANCH       Branch of the coderecipe
  
  mdswitch (switch qualitylevel for domain) and mddisabledebug (disable debug for domain):
    --qualitylevel QUALITYLEVEL
                          Qualitylevel to switch to or to put disable debug.
  
  addrepo:
    -ql QL                Qualitylevel to use for metadata.
    -bba BBA              Bitbucket account e.g. jumpscale,incubaid.
    -bbr BBR              Bitbucket reponame e.g. serverapps (there will be jp_
                          prepended)



update metadata
===============




.. code-block:: python

  template:shell
  #updates the metadata
  jpackage mdupdate
  
  #updates metadata removes changes made to the metadata (locally)
  jpackage mdupdate --force



install or update jpackage
==========================




.. code-block:: python

  template:shell
  #updates selected jpackages
  jpackage install
  
  #updates selected jpackages from domain jumpscale
  jpackage install -d jumpscale
  
  #select osis and all dependencies on osis and reinstall each found jpackage (so also the dependencies)
  jpackage install -n osis --deps -r
  
  #select osis and all dependencies on osis and install each found jpackage, the package will only be effectively installed if buildnr changes
  jpackage install -n osis --deps 
  
  #select osis, install osis and its dependencies
  jpackage install -n osis 
  
  #select osis, install osis and its dependencies, ONLY osis will be reinstalled independant if buildnr changed 
  #(id you want deps as well to reinstall use --deps)
  jpackage install -n osis -r
  
  #do only install osis, do not look at dependencies
  jpackage install -n osis -s
  
  #Install with hrd configuration
  jpackage install -n redis -i system --data 'redis.name:system redis.port:7766 redis.disk:0 redis.mem:100'
  #whatever you pass with --data is used to populate the hrd of the instance


updating or installing is in fact same operation


debug
=====


* some examples how to manipulate debug flag of jpackages
* a jpackage in debug will always be installed automatically from code




.. code-block:: python

  template:shell
  #list all jpackages in debug
  jpackage debug --list
  
  #asks domain then the jpackage and then enables debug
  jpackage debug --enable
  
  #list all jpackages which are in debug, ask which ones to disable
  jpackage debug --disable



