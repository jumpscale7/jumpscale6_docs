
j.dirs
======


* path: /core/Dirs.py


Utility class to configure and store all relevant directory paths


addProtectedDir
---------------


* params: path,name
* path:/core/Dirs.py (line:255)


checkInProtectedDir
-------------------


* params: path
* path:/core/Dirs.py (line:288)


deployDefaultFilesInSandbox
---------------------------


* params:
* path:/core/Dirs.py (line:295)


getPathOfRunningFunction
------------------------


* params: function
* path:/core/Dirs.py (line:234)


init
----


* params: reinit
* path:/core/Dirs.py (line:191)


Initializes all the configured directories if needed

If a folder attribute is None, set its value to the corresponding
default path.



loadProtectedDirs
-----------------


* params:
* path:/core/Dirs.py (line:237)


removeProtectedDir
------------------


* params: path
* path:/core/Dirs.py (line:267)


replaceFilesDirVars
-------------------


* params: path,recursive,filter,additionalArgs
* path:/core/Dirs.py (line:179)


replaceTxtDirVars
-----------------


* params: txt,additionalArgs
* path:/core/Dirs.py (line:158)


replace $base,$vardir,$cfgdir,$bindir,$codedir,$tmpdir,$logdir,$appdir with props of this class


