
j.system.ovsnetconfig
=====================


* path: /lib/ovsnetconfig/NetConfigFactory.py


applyconfig
-----------


* params: interfacenameToExclude,backplanename
* path:/lib/ovsnetconfig/NetConfigFactory.py (line:321)


DANGEROUS, will remove old configuration


configureStaticAddress
----------------------


* params: interfacename,ipaddr,gw
* path:/lib/ovsnetconfig/NetConfigFactory.py (line:175)


Configure a static address


createVXLanBridge
-----------------


* params: networkid,backend,bridgename
* path:/lib/ovsnetconfig/NetConfigFactory.py (line:105)


Creates a proper vxlan interface and bridge based on a backplane


ensureVXNet
-----------


* params: networkid,backend
* path:/lib/ovsnetconfig/NetConfigFactory.py (line:98)


getConfigFromSystem
-------------------


* params: reload
* path:/lib/ovsnetconfig/NetConfigFactory.py (line:19)


walk over system and get configuration, result is dict


getType
-------


* params: interfaceName
* path:/lib/ovsnetconfig/NetConfigFactory.py (line:118)


initNetworkInterfaces
---------------------


* params:
* path:/lib/ovsnetconfig/NetConfigFactory.py (line:71)


Resets /etc/network/interfaces with a basic configuration


loadNetworkInterfaces
---------------------


* params:
* path:/lib/ovsnetconfig/NetConfigFactory.py (line:77)


Reloads the networking configuration which is basicly applying /etc/network/interfaces


newBondedBackplane
------------------


* params: name,interfaces,trunks
* path:/lib/ovsnetconfig/NetConfigFactory.py (line:344)


Reasonable defaults  : mode=balance-tcp, lacp=active,fast, bondname=brname-Bond, all vlans allowed


newBridge
---------


* params: name,interface
* path:/lib/ovsnetconfig/NetConfigFactory.py (line:86)



newVlanBridge
-------------


* params: name,parentbridge,vlanid,mtu
* path:/lib/ovsnetconfig/NetConfigFactory.py (line:95)


printConfigFromSystem
---------------------


* params:
* path:/lib/ovsnetconfig/NetConfigFactory.py (line:83)


removeOldConfig
---------------


* params:
* path:/lib/ovsnetconfig/NetConfigFactory.py (line:34)


setBackplane
------------


* params: interfacename,backplanename,ipaddr,gw
* path:/lib/ovsnetconfig/NetConfigFactory.py (line:239)


DANGEROUS, will remove old configuration


setBackplaneDhcp
----------------


* params: interfacename,backplanename
* path:/lib/ovsnetconfig/NetConfigFactory.py (line:127)


DANGEROUS, will remove old configuration


setBackplaneNoAddress
---------------------


* params: interfacename,backplanename
* path:/lib/ovsnetconfig/NetConfigFactory.py (line:152)


DANGEROUS, will remove old configuration


setBackplaneNoAddressWithBond
-----------------------------


* params: bondname,bondinterfaces,backplanename
* path:/lib/ovsnetconfig/NetConfigFactory.py (line:202)


DANGEROUS, will remove old configuration


setBackplaneWithBond
--------------------


* params: bondname,bondinterfaces,backplanename,ipaddr,gw
* path:/lib/ovsnetconfig/NetConfigFactory.py (line:275)


DANGEROUS, will remove old configuration


