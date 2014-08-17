
j.system.platform.diskmanager
=============================


* path: /lib/diskmanager/Diskmanager.py


diskGetFreeRegions
------------------


* params: disk,align
* path:/lib/diskmanager/Diskmanager.py (line:110)


Get a filtered list of free regions, excluding the gaps due to partition alignment


mirrorsFind
-----------


* params:
* path:/lib/diskmanager/Diskmanager.py (line:122)


partitionAdd
------------


* params: disk,free,align,length,fs_type,type
* path:/lib/diskmanager/Diskmanager.py (line:82)


partitionsFind
--------------


* params: mounted,ttype,ssd,prefix,minsize,maxsize,devbusy,initialize,forceinitialize
* path:/lib/diskmanager/Diskmanager.py (line:127)


looks for disks which are know to be data disks & are formatted ext4
return [$partpath,$size,$free,$ssd <$partpath,$size,$free,$ssd>]


partitionsFind_Ext4Data
-----------------------


* params:
* path:/lib/diskmanager/Diskmanager.py (line:264)


looks for disks which are know to be data disks & are formatted ext4
return [$partpath,$gid,$partid,$size,$free <$partpath,$gid,$partid,$size,$free>]


partitionsGetMounted_Ext4Data
-----------------------------


* params:
* path:/lib/diskmanager/Diskmanager.py (line:286)


find disks which are mounted


partitionsMount_Ext4Data
------------------------


* params:
* path:/lib/diskmanager/Diskmanager.py (line:272)


partitionsUnmount_Ext4Data
--------------------------


* params:
* path:/lib/diskmanager/Diskmanager.py (line:279)


