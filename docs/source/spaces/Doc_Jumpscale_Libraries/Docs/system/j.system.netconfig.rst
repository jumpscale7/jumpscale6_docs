
j.system.netconfig
==================


* path: /baselib/netconfig/Netconfig.py




addIpToInterface
----------------


* params: dev,ipaddr,aliasnr,start
* path:/baselib/netconfig/Netconfig.py (line:184)


enableInterface
---------------


* params: dev,start,dhcp
* path:/baselib/netconfig/Netconfig.py (line:60)


enableInterfaceBridgeDhcp
-------------------------


* params: dev,bridgedev,start
* path:/baselib/netconfig/Netconfig.py (line:168)




enableInterfaceBridgeStatic
---------------------------


* params: dev,ipaddr,bridgedev,gw,start
* path:/baselib/netconfig/Netconfig.py (line:126)


ipaddr in form of 192.168.10.2/24 (can be list)
gateway in form of 192.168.10.254


enableInterfaceStatic
---------------------


* params: dev,ipaddr,gw,start
* path:/baselib/netconfig/Netconfig.py (line:106)


ipaddr in form of 192.168.10.2/24 (can be list)
gateway in form of 192.168.10.254


remove
------


* params: dev
* path:/baselib/netconfig/Netconfig.py (line:84)


reset
-----


* params: shutdown
* path:/baselib/netconfig/Netconfig.py (line:49)


empty config of /etc/network/interfaces


setNameserver
-------------


* params: addr
* path:/baselib/netconfig/Netconfig.py (line:91)


resolvconf will be disabled


setRoot
-------


* params: root
* path:/baselib/netconfig/Netconfig.py (line:15)


shutdownNetwork
---------------


* params: excludes
* path:/baselib/netconfig/Netconfig.py (line:23)


find all interfaces and shut them all down with ifdown
this is to remove all networking things going on


