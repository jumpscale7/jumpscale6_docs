
j.config
========


* path: /core/config/JConfig.py


jumpscale singleton class available under j.config
Meant for non interactive access to configuration items


getConfig
---------


* params: configtype,directory
* path:/core/config/JConfig.py (line:14)


Return dict of dicts for this configuration.
E.g. { 'jumpscale.org'    : {url:'http://jumpscale.org', login='test'} ,
'trac.qlayer.com' : {url:'http://trac.qlayer.com', login='mylogin'} }


getInifile
----------


* params: configtype,directory
* path:/core/config/JConfig.py (line:10)


list
----


* params:
* path:/core/config/JConfig.py (line:26)


List all configuration types available.


remove
------


* params: configtype,directory
* path:/core/config/JConfig.py (line:23)


