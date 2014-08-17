
j.servers.base
==============


* path: /grid/serverbase/ServerBaseFactory.py


getDaemon
---------


* params: name,sslorg,ssluser,sslkeyvaluestor
* path:/grid/serverbase/ServerBaseFactory.py (line:10)


is the basis for every daemon we create which can be exposed over e.g. zmq or sockets or http


daemon=j.servers.base.getDaemon()

class MyCommands():
def __init__(self,daemon):
self.daemon=daemon

def pingcmd(self,session=session):
return "pong"

def echo(self,msg="",session=session):
return msg

daemon.addCMDsInterface(MyCommands,category="optional")  #pass as class not as object !!! chose category if only 1 then can leave ""



getDaemonClientClass
--------------------


* params:
* path:/grid/serverbase/ServerBaseFactory.py (line:56)


example usage, see example for server at self.getDaemon (implement transport still)

DaemonClientClass=j.servers.base.getDaemonClientClass()

myClient(DaemonClientClass):
def __init__(self,ipaddr="127.0.0.1",port=5651,org="myorg",user="root",passwd="1234",ssl=False,roles=[]):
self.init(org=org,user=user,passwd=passwd,ssl=ssl,roles=roles)

def _connect(self):
pass

def _close(self):
pass


def _sendMsg(self, cmd,data,sendformat="m",returnformat="m"):
pass

client=myClient()
print client.echo("atest")


initSSL4Server
--------------


* params: organization,serveruser,sslkeyvaluestor
* path:/grid/serverbase/ServerBaseFactory.py (line:51)


