
j.core.zdaemon
==============


* path: /grid/zdaemon/ZDaemonFactory.py


getZDaemon
----------


* params: port,name,nrCmdGreenlets,sslorg,ssluser,sslkeyvaluestor
* path:/grid/zdaemon/ZDaemonFactory.py (line:9)


is a generic usable zmq daemon which has a data & cmd channel (data channel not completely implemented for now)


zd=j.core.zdaemon.getZDaemon(port=5651,nrCmdGreenlets=50)

class MyCommands():
def __init__(self,daemon):
self.daemon=daemon

def pingcmd(self,session=None):
return "pong"

def echo(self,msg="",session=None):
return msg

be used in method

zd.addCMDsInterface(MyCommands)  #pass as class not as object !!!
zd.start()

use self.getZDaemonClientClass as client to this daemon


getZDaemonAgent
---------------


* params: ipaddr,port,org,user,passwd,ssl,reset,roles
* path:/grid/zdaemon/ZDaemonFactory.py (line:86)


example usage, see example for server at self.getZDaemon

agent=j.core.zdaemon.getZDaemonAgent(ipaddr="127.0.0.1",port=5651,login="root",passwd="1234",ssl=False,roles="*" <"*">)
agent.start()


* means all


getZDaemonClient
----------------


* params: addr,port,org,user,passwd,ssl,category,sendformat,returnformat,gevent
* path:/grid/zdaemon/ZDaemonFactory.py (line:40)


example usage, see example for server at self.getZDaemon

client=j.core.zdaemon.getZDaemonClient(ipaddr="127.0.0.1",port=5651,login="root",passwd="1234",ssl=False)

print client.echo("Hello World.")


getZDaemonHAClient
------------------


* params: connections,org,user,passwd,ssl,category,sendformat,returnformat,gevent
* path:/grid/zdaemon/ZDaemonFactory.py (line:56)


example usage, see example for server at self.getZDaemon

client=j.core.zdaemon.getZDaemonHAClient(('127.0.0.1', 5544) <('127.0.0.1', 5544)>,login="root",passwd="1234",ssl=False)

print client.echo("Hello World.")


getZDaemonTransportClass
------------------------


* params:
* path:/grid/zdaemon/ZDaemonFactory.py (line:71)


import JumpScale.grid.zdaemon
class BlobStorTransport(j.core.zdaemon.getZDaemonTransportClass()):
def sendMsg(self,timeout=0, *args):
self._cmdchannel.send_multipart(args)
result=self._cmdchannel.recv_multipart()
return result
transp=BlobStorTransport(addr=ipaddr,port=port,gevent=True)


initSSL4Server
--------------


* params: organization,serveruser,sslkeyvaluestor
* path:/grid/zdaemon/ZDaemonFactory.py (line:102)


use this to init your ssl keys for the server (they can be used over all transports)


