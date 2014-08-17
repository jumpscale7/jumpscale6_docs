
j.core.portal
=============


* path: /portal/portal/PortalFactory.py


getClient
---------


* params: ip,port,secret
* path:/portal/portal/PortalFactory.py (line:55)


return client to manipulate & access a running application server (out of process)
caching is done so can call this as many times as required
secret is normally configured from grid
there is normally no need to use this method, use self.getActorClient in stead


getPortalConfig
---------------


* params: appname
* path:/portal/portal/PortalFactory.py (line:26)


getServer
---------


* params:
* path:/portal/portal/PortalFactory.py (line:23)


loadActorsInProcess
-------------------


* params:
* path:/portal/portal/PortalFactory.py (line:30)


make sure all actors are loaded on j.apps...


