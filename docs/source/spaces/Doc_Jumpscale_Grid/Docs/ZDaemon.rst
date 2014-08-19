

ZDaemon
*******

* Send RPC
* Send Binary


ZDaemon Client
==============


Currently two clients are offered:


* One raw client which requires sending commands as string
* A command client which exposes commands as methods (retrieved by introspection)


Raw client
==========




.. code-block:: python

  #!python
  import OpenWizzy,grid
  cl = j.core.grid.getZDaemonClientClass()(port=9445)
  
  cl.blocksize                  cl.init                       cl.receivefile                cl.sendbinary
  cl.close                      cl.ipaddr                     cl.reset                      cl.sendblock
  cl.cmdchannel                 cl.perftest                   cl.retry                      cl.sendcmd
  cl.context                    cl.poll                       cl.sendMsgOverCMDChannel      cl.sendfile
  cl.datachannel                cl.port                       cl.sendMsgOverCMDChannelFast  cl.servername


The client exposes all raw methods of the ZDaemon interface.


CMD (introspection) client
==========================





.. code-block:: python

  #!python
  from OpenWizzy.grid.zdaemon.ZDaemonClient import ZDaemonCmdClient
  cl = ZDaemonCmdClient(port=5544) # connect to osis
  
  cl.createNamespace          cl.get                      cl.listNamespaceCategories  cl.pingcmd
  cl.createNamespaceCategory  cl.getNameIDsInfoAll        cl.listNamespaces           cl.search
  cl.delete                   cl.getfreeport              cl.log                      cl.set
  cl.echo                     cl.list                     cl.logeco


The arguments and docstring are synced from the server commands provided that it inherits from `from OpenWizzy.grid.zdaemon.ZDaemonCMDS import ZDaemonCMDS`
