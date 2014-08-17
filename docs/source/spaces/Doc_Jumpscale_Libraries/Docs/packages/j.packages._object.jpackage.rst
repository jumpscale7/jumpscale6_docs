
j.packages._object.jpackage
===========================


* path: /baselib/jpackages/JPackageObject.py


Data representation of a JPackage, should contain all information contained in the jpackages.cfg


addDependency
-------------


* params: domain,name,supportedplatforms,minversion,maxversion,dependencytype
* path:/baselib/jpackages/JPackageObject.py (line:535)


backup
------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:15)


buildNrIncrement
----------------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:670)


checkExistingBlobs
------------------


* params: blobserver,dependencies
* path:/baselib/jpackages/JPackageObject.py (line:1727)



codeCommit
----------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:15)


codeExport
----------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:15)


codeLink
--------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:15)


codeUpdate
----------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:15)


compile
-------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:15)


configure
---------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:15)


copyfiles
---------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:15)


delete
------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:15)


download
--------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:15)


getBlobHistory
--------------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:1746)


getBlobInfo
-----------


* params: platform,ttype,active
* path:/baselib/jpackages/JPackageObject.py (line:745)



getBlobItemPaths
----------------


* params: platform,ttype,blobitempath
* path:/baselib/jpackages/JPackageObject.py (line:766)


translates the item as shown in the blobinfo to the corresponding paths (jpackageFilesPath,destpathOnSystem)


getBlobKeysActive
-----------------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:1661)


getBlobPlatformTypes
--------------------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:15)


getBrokenDependencies
---------------------


* params: platform
* path:/baselib/jpackages/JPackageObject.py (line:703)


Return a list of dependencies that cannot be resolved


getCodeLocationsFromRecipe
--------------------------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:800)


getCodeMgmtRecipe
-----------------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:268)


getDebugMode
------------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:369)


getDebugModeInJpackage
----------------------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:372)


getDependencies
---------------


* params: errorIfNotFound
* path:/baselib/jpackages/JPackageObject.py (line:719)


Return the dependencies for the JPackage


getDependingInstalledPackages
-----------------------------


* params: recursive,errorIfNotFound
* path:/baselib/jpackages/JPackageObject.py (line:565)


Return the packages that are dependent on this packages and installed on this machine
This is a heavy operation and might take some time


getDependingPackages
--------------------


* params: recursive,errorIfNotFound
* path:/baselib/jpackages/JPackageObject.py (line:575)


Return the packages that are dependent on this package
This is a heavy operation and might take some time


getHighestInstalledBuildNr
--------------------------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:663)


Return the latetst installed buildnumber


getInstanceNames
----------------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:726)


getIsPreparedForUpdatingFiles
-----------------------------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:553)


Return true if package has been prepared


getKey
------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:562)


getMetadataPathQualityLevel
---------------------------


* params: ql
* path:/baselib/jpackages/JPackageObject.py (line:685)


getPathFiles
------------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:619)


Return absolute pathname of the jpackages's filespath


getPathFilesPlatform
--------------------


* params: platform
* path:/baselib/jpackages/JPackageObject.py (line:626)


Return absolute pathname of the jpackages's filespath
if not given then will be: j.system.platformtype


getPathFilesPlatformForSubDir
-----------------------------


* params: subdir
* path:/baselib/jpackages/JPackageObject.py (line:638)


Return absolute pathnames of the jpackages's filespath for platform or parent of platform if it does not exist in lowest level
if platform not given then will be: j.system.platformtype
the subdir will be used to check upon if found in one of the dirs, if never found will raise error
all matching results are returned


getPathInstance
---------------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:607)


Return absolute pathname of the package's metadatapath


getPathMetadata
---------------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:613)


Return absolute pathname of the package's metadatapath active instance


getPathSourceCode
-----------------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:656)


Return absolute path to where this package's source can be extracted to


getQualityLevels
----------------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:695)


getVersionAsInt
---------------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:598)


Translate string version representation to a number


hasModifiedFiles
----------------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:868)


Check if files are modified in the JPackage files


hasModifiedMetaData
-------------------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:877)


Check if files are modified in the JPackage metadata


install
-------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:15)


installDebs
-----------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:1086)


isInstalled
-----------


* params: instance,checkAndDie,hrdcheck
* path:/baselib/jpackages/JPackageObject.py (line:884)


Check if the JPackage is installed


isNew
-----


* params:
* path:/baselib/jpackages/JPackageObject.py (line:1235)


isPendingReconfiguration
------------------------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:1907)


Check if the JPackage needs reconfiguration


isrunning
---------


* params: dependencies,ipaddr
* path:/baselib/jpackages/JPackageObject.py (line:1047)


Check if application installed is running for jpackages


kill
----


* params:
* path:/baselib/jpackages/JPackageObject.py (line:15)


load
----


* params: instance,force,hrddata,findDefaultInstance
* path:/baselib/jpackages/JPackageObject.py (line:209)


loadBlobStores
--------------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:357)


loadDependencies
----------------


* params: errorIfNotFound
* path:/baselib/jpackages/JPackageObject.py (line:489)


log
---


* params: msg,category,level
* path:/baselib/jpackages/JPackageObject.py (line:130)


monitor
-------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:15)


monitor_net
-----------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:15)


package
-------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:15)


prepare
-------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:15)


prepareForUpdatingFiles
-----------------------


* params: suppressErrors
* path:/baselib/jpackages/JPackageObject.py (line:1266)


After this command the operator can change the files of the jpackages.
Files do not aways come from code repo, they can also come from jpackages repo only


processDepCheck
---------------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:15)


reinstall
---------


* params: dependencies,download
* path:/baselib/jpackages/JPackageObject.py (line:1055)


Reinstall the JPackage by running its install tasklet, best not to use dependancies reinstall


removeDebugMode
---------------


* params: dependencies
* path:/baselib/jpackages/JPackageObject.py (line:410)


removeDebugModeInJpackage
-------------------------


* params: dependencies
* path:/baselib/jpackages/JPackageObject.py (line:400)


reportNumbers
-------------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:1994)


restart
-------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:15)


restore
-------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:15)


save
----


* params:
* path:/baselib/jpackages/JPackageObject.py (line:15)


setDebugMode
------------


* params: dependencies
* path:/baselib/jpackages/JPackageObject.py (line:378)


setDebugModeInJpackage
----------------------


* params: dependencies
* path:/baselib/jpackages/JPackageObject.py (line:391)


showDependencies
----------------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:1919)


Return all dependencies of the JPackage.
See also: addDependency and removeDependency


showDependingInstalledPackages
------------------------------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:1926)


Show which jpackages have this jpackages as dependency.
Do this only for the installed jpackages.


showDependingPackages
---------------------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:1933)


Show which jpackages have this jpackages as dependency.


signalConfigurationNeeded
-------------------------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:1900)


Set in the corresponding jpackages's state file if reconfiguration is needed


start
-----


* params:
* path:/baselib/jpackages/JPackageObject.py (line:15)


stop
----


* params:
* path:/baselib/jpackages/JPackageObject.py (line:15)


supportsPlatform
----------------


* params: platform
* path:/baselib/jpackages/JPackageObject.py (line:905)


Check if a JPackage can be installed on a platform


uninstall
---------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:15)


upload
------


* params: remote,local,dependencies,onlycode
* path:/baselib/jpackages/JPackageObject.py (line:1646)


uploadExistingBlobs
-------------------


* params: blobserver,dependencies
* path:/baselib/jpackages/JPackageObject.py (line:1668)



uploadExistingBlobsFromHistory
------------------------------


* params: blobserver
* path:/baselib/jpackages/JPackageObject.py (line:1698)



waitDown
--------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:15)


waitUp
------


* params:
* path:/baselib/jpackages/JPackageObject.py (line:15)


