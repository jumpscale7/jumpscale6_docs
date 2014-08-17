
j.servers.tipc
==============


* path: /grid/tipc/TipcFactory.py


getClient
---------


* params: servaddr,category,org,user,passwd,ssl,roles
* path:/grid/tipc/TipcFactory.py (line:30)


getServer
---------


* params: servaddr,sslorg,ssluser,sslkeyvaluestor
* path:/grid/tipc/TipcFactory.py (line:6)


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


