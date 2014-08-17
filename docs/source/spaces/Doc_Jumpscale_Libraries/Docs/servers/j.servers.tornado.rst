
j.servers.tornado
=================


* path: /grid/tornado/TornadoFactory.py


getClient
---------


* params: addr,port,category,org,user,passwd,ssl,roles
* path:/grid/tornado/TornadoFactory.py (line:30)


getServer
---------


* params: port,sslorg,ssluser,sslkeyvaluestor
* path:/grid/tornado/TornadoFactory.py (line:6)


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
* path:/grid/tornado/TornadoFactory.py (line:37)


use this to init your ssl keys for the server (they can be used over all transports)


