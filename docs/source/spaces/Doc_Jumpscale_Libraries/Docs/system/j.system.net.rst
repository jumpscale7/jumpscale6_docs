
j.system.net
============


* path: /core/system/net.py


checkIpAddressIsLocal
---------------------


* params: ipaddr
* path:/core/system/net.py (line:234)


checkListenPort
---------------


* params: port
* path:/core/system/net.py (line:105)


Check if a certain port is listening on the system.



checkUrlReachable
-----------------


* params: url
* path:/core/system/net.py (line:88)


raise operational critical if unreachable
return True if reachable


download
--------


* params: url,localpath,username,passwd
* path:/core/system/net.py (line:805)


Download a url to a file or a directory, supported protocols: http, https, ftp, file


enableProxy
-----------


* params:
* path:/core/system/net.py (line:240)


getDefaultRouter
----------------


* params:
* path:/core/system/net.py (line:652)


Get default router


getDomainName
-------------


* params:
* path:/core/system/net.py (line:853)


Retrieve the dns domain name


getHostByName
-------------


* params: dnsHostname
* path:/core/system/net.py (line:649)


getHostNamesForIP
-----------------


* params: hostsfile,ip
* path:/core/system/net.py (line:766)


Get hostnames for ip address


getHostname
-----------


* params:
* path:/core/system/net.py (line:612)


Get hostname of the machine



getIpAddress
------------


* params: interface
* path:/core/system/net.py (line:452)


Return a list of ip addresses and netmasks assigned to this interface


getIpAddresses
--------------


* params: up
* path:/core/system/net.py (line:219)


getMacAddress
-------------


* params: interface
* path:/core/system/net.py (line:503)


Return the MAC address of this interface


getMacAddressForIp
------------------


* params: ipaddress
* path:/core/system/net.py (line:555)


Search the MAC address of the given IP address in the ARP table



getNameServer
-------------


* params:
* path:/core/system/net.py (line:189)


Returns the first nameserver IP found in /etc/resolv.conf

Only implemented for Unix based hosts.




getNetworkInfo
--------------


* params:
* path:/core/system/net.py (line:434)


returns {macaddr_name:ipaddr,ipaddr <ipaddr,ipaddr>,...}


getNicType
----------


* params: interface
* path:/core/system/net.py (line:299)


Get Nic Type on a certain interface


getNics
-------


* params: up
* path:/core/system/net.py (line:261)


Get Nics on this machine
Works only for Linux/Solaris systems


getReachableIpAddress
---------------------


* params: ip,port
* path:/core/system/net.py (line:424)


Returns the first local ip address that can connect to the specified ip on the specified port


getVlanTag
----------


* params: interface,nicType
* path:/core/system/net.py (line:370)


Get VLan tag on the specified interface and vlan type


getVlanTagFromInterface
-----------------------


* params: interface
* path:/core/system/net.py (line:393)


Get vlan tag from interface


isIpInHostsFile
---------------


* params: hostsfile,ip
* path:/core/system/net.py (line:738)


Check if ip is in the hostsfile


isIpLocal
---------


* params: ipaddress
* path:/core/system/net.py (line:550)


isNicConnected
--------------


* params: interface
* path:/core/system/net.py (line:617)


pingMachine
-----------


* params: ip,pingtimeout,recheck,allowhostname
* path:/core/system/net.py (line:696)


Ping a machine to check if it's up/running and accessible


pm_formatMacAddress
-------------------


* params: macaddress
* path:/core/system/net.py (line:540)


removeFromHostsFile
-------------------


* params: hostsfile,ip
* path:/core/system/net.py (line:751)


Update a hostfile, delete ip from hostsfile


tcpPortConnectionTest
---------------------


* params: ipaddr,port,timeout
* path:/core/system/net.py (line:37)


updateHostsFile
---------------


* params: hostsfile,ip,hostname
* path:/core/system/net.py (line:783)


Update a hostfile to contain the basic information install


validateIpAddress
-----------------


* params: ipaddress
* path:/core/system/net.py (line:667)


Validate wether this ip address is a valid ip address of 4 octets ranging from 0 to 255 or not


waitConnectionTest
------------------


* params: ipaddr,port,timeout
* path:/core/system/net.py (line:52)


will return false if not successfull (timeout)


waitConnectionTestStopped
-------------------------


* params: ipaddr,port,timeout
* path:/core/system/net.py (line:71)


will test that port is not active
will return false if not successfull (timeout)


