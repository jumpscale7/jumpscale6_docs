

how to install sentry
*********************


sentry is a bug/event mgmt system.

prefer to install it in a separate LXC instance (use jsmachine)




.. code-block:: python

  jpackage install -n sentry


go to $ipaddr:9000

default login/passwd: admin/admin


to reconfigure
--------------




.. code-block:: python

  # jpackage configure -n sentry
  sandbox:/opt/jsbox
  jpackage_                 :: JPackage jumpscale sentry 1.0:configure
  sentry              : no need to start, already started.
  SENTRY_DSN for Default = "c1c6481f48704f4c8dd9f8ff3bd14d69:bfd1246d660a4cb6b531b0f1c6ade41d"
  SENTRY_DSN for Ops = "8b0bb43402ab4721b18dcbc9a89bb30d:c156e1abd376444eb5d8030f5af4c7ec"
  SENTRY_DSN for Bugs = "eead18c0f0574773b60ab5e67ca47efb:47c39980f24a41ae865b66a3c7be739e"




configure you client for it
---------------------------


in this example our sentry is on 192.168.1.40




.. code-block:: python

  #check the DSN
  firefox http://192.168.1.40:9000/default/default/keys/


unsupported image:/images/unknownspace/sentry_dsn.png
!sentry_dsn.png!




.. code-block:: python

  http://1351b1f4d4c049c59e35c2d0c2bc43b9:d648a21dd00a4b9e89d08e51d1da86ce@192.168.1.40:9000/2
  '{PROTOCOL}://{PUBLIC_KEY}:{SECRET_KEY}@{HOST}/{PATH}{PROJECT_ID}'


the first part = public key
the 2nd part = secret key
the /2 = the project id






.. code-block:: python

  #install the client
  # jpackage install -n sentry_client
  sandbox:/opt/jsbox
  jpackage_init             :: JPackage jumpscale sentry_client 1.0:did not find active hrd for /opt/jsbox_data/cfg/hrd/sentry.hrd, will now put there
  Please provide value for sentry.public_key [18275531e40849ae8f259a4edd8f1c22]: 1351b1f4d4c049c59e35c2d0c2bc43b9
  Please provide value for sentry.secret_key [d43b0396addb4b789cd6c325a9ceb36e]: d648a21dd00a4b9e89d08e51d1da86ce
  Please provide value for sentry.server [127.0.0.1]: 192.168.1.40
  Please provide value for sentry.project [2]: 2
  jpackage_                 :: JPackage jumpscale sentry_client 1.0:stop sentry_client
  jpackage_                 :: JPackage jumpscale sentry_client 1.0:stop
  jpackage_                 :: JPackage jumpscale sentry_client 1.0:Downloading.
  exists 494f59dce4c4d3eac1b2e0269f9fd6e8:  True
  jpackage_download         :: JPackage jumpscale sentry_client 1.0:expand platform_type:linux64_sitepackages
  exists 494f59dce4c4d3eac1b2e0269f9fd6e8:  True
  jpackage_                 :: JPackage jumpscale sentry_client 1.0:installing
  jpackage_                 :: JPackage jumpscale sentry_client 1.0:copy files from:/opt/jsbox_data/var/jpackages/files/jumpscale/sentry_client/1.0/linux64/sitepackages to:/opt/jsbox/libext/
  pathplatform:/opt/jsbox_data/var/jpackages/files/jumpscale/sentry_client/1.0/linux64/sitepackages
  jpackage_                 :: JPackage jumpscale sentry_client 1.0:configure



to test
-------




.. code-block:: python

  pip install raven --upgrade
  raven test http://1351b1f4d4c049c59e35c2d0c2bc43b9:d648a21dd00a4b9e89d08e51d1da86ce@192.168.1.40:9000/2


return something like



.. code-block:: python

  Using DSN configuration:
    http://1351b1f4d4c049c59e35c2d0c2bc43b9:d648a21dd00a4b9e89d08e51d1da86ce@192.168.1.40:9000/2
  
  Client configuration:
    servers        : ['http://192.168.1.40:9000/api/2/store/']
    project        : 2
    public_key     : 1351b1f4d4c049c59e35c2d0c2bc43b9
    secret_key     : d648a21dd00a4b9e89d08e51d1da86ce
  
  Sending a test message... success!
  Event ID was 'ffb2db96b9b3461eaabea10255f73149'

