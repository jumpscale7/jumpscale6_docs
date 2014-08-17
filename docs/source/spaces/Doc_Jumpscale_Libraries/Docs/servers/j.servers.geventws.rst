
j.servers.geventws
==================


* path: /grid/geventws/GeventWSFactory.py


getClient
---------


* params: addr,port,category,org,user,passwd,ssl,roles,id,timeout
* path:/grid/geventws/GeventWSFactory.py (line:33)


getHAClient
-----------


* params: connections,category,org,user,passwd,ssl,roles,id,timeout
* path:/grid/geventws/GeventWSFactory.py (line:53)


getServer
---------


* params: port,sslorg,ssluser,sslkeyvaluestor
* path:/grid/geventws/GeventWSFactory.py (line:9)


HOW TO USE:
daemon=j.servers.tornado.getServer(port=4444)

class MyCommands():
def __init__(self,daemon):
self.daemon=daemon

def pingcmd(self,session=session):
return "pong"

def echo(self,msg="",session=session):
return msg

daemon.addCMDsInterface(MyCommands,category="optional")  #pass as class not as object !!! chose category if only 1 then can leave ""

daemon.start()


initSSL4Server
--------------


* params: organization,serveruser,sslkeyvaluestor
* path:/grid/geventws/GeventWSFactory.py (line:73)


use this to init your ssl keys for the server (they can be used over all transports)


