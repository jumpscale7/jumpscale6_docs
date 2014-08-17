
j.packages.releaseMgmt
======================


* path: /baselib/jpackages/ReleaseMgmt.py



createTgzForChangedPackages
---------------------------


* params: earlierFile,laterFile,tempDir,tarName
* path:/baselib/jpackages/ReleaseMgmt.py (line:127)


Given two files with a list of packages, this method will download to a temporary folder the packages that have been added to laterFile.
Each package will be downloaded in a subdirectory corresponding to its domain.
Packages will be downloaded for all platforms.
Next to the packages, the metadata will be copied as well to the temporary folder.
Finally the folders and files will be compressed in a tgz file
Note that the packages and metadata are downloaded from the location specified in bundledownload in /opt/qbase3/cfg/jpackages/sources.cfg
If there are no changes between the two package files, an empty tgz file will be created.

Parameters:
- earlierFile: string - file containing the packages for an earlier release
- laterFile: string - file containing the packages for a later release. Added packages will be given back by this method if comparison = '+'
- tempDir: string - temporary directory where files will be downloaded. This directory will be cleaned up at the beginning of the method and must be located in an existing directory!
- tarName: string - name of the tgz file to be created

Returns:
None


generateBillOfMaterials
-----------------------


* params: jpackagesObject,outputFile
* path:/baselib/jpackages/ReleaseMgmt.py (line:41)


Create a file with all jpackages and their versions that a given jpackages depends upon ('parents')
The file will contain the domain, the name, the version and the build nr from the parent jpackages.
The file will be sorted.

Parameters:
- jpackagesObject: Object - the jpackages object where you want to list the parents for
- outputFile: string - the file where the parent jpackages list will be written to

Returns: None


listChangedPackagesAsStrings
----------------------------


* params: earlierFile,laterFile,comparison
* path:/baselib/jpackages/ReleaseMgmt.py (line:78)


Given two files with a list of packages, this method will give back the packages that have been added or removed between the two.

Parameters:
- earlierFile: string - file containing the packages for an earlier release
- laterFile: string - file containing the packages for a later release. Added packages will be given back by this method if comparison = '+'
- comparison: char - '+' if you want the added packages back. '-' if you want the removed packages back.

Returns:
list of strings - each string is the name of a package


