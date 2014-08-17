
j.packages.sourcesConfig
========================


* path: /baselib/inifile/IniFile.py


Use with care:
- addParam and setParam are 'auto-write'
- addSection isn't
- removeSection isn't
- removeParam isn't


addParam
--------


* params: sectionName,paramName,newvalue
* path:/baselib/inifile/IniFile.py (line:204)


Add name-value pair to section of IniFile


addSection
----------


* params: sectionName
* path:/baselib/inifile/IniFile.py (line:191)


Add a new section to this Inifile. If it already existed, silently pass


checkParam
----------


* params: sectionName,paramName
* path:/baselib/inifile/IniFile.py (line:132)


Boolean indicating whether parameter exists under this section in the IniFile


checkSection
------------


* params: sectionName
* path:/baselib/inifile/IniFile.py (line:124)


Boolean indicating whether section exists in this IniFile


getBooleanValue
---------------


* params: sectionName,paramName
* path:/baselib/inifile/IniFile.py (line:157)


Get boolean value of the specified parameter


getContent
----------


* params:
* path:/baselib/inifile/IniFile.py (line:285)


Get the Inifile content to a string



getFileAsDict
-------------


* params:
* path:/baselib/inifile/IniFile.py (line:310)


getFloatValue
-------------


* params: sectionName,paramName
* path:/baselib/inifile/IniFile.py (line:180)


Get float value of the specified parameter


getIntValue
-----------


* params: sectionName,paramName
* path:/baselib/inifile/IniFile.py (line:169)


Get an integer value of the specified parameter


getParams
---------


* params: sectionName
* path:/baselib/inifile/IniFile.py (line:115)


Return list of params in a certain section of this IniFile


getSectionAsDict
----------------


* params: section
* path:/baselib/inifile/IniFile.py (line:304)


getSections
-----------


* params:
* path:/baselib/inifile/IniFile.py (line:108)


Return list of sections from this IniFile


getValue
--------


* params: sectionName,paramName,raw,default
* path:/baselib/inifile/IniFile.py (line:141)


Get value of the parameter from this IniFile


removeParam
-----------


* params: sectionName,paramName
* path:/baselib/inifile/IniFile.py (line:241)


Remove a param from this IniFile


removeSection
-------------


* params: sectionName
* path:/baselib/inifile/IniFile.py (line:228)


Remove a section from this IniFile


setParam
--------


* params: sectionName,paramName,newvalue
* path:/baselib/inifile/IniFile.py (line:221)


Add name-value pair to section of IniFile


write
-----


* params: filePath
* path:/baselib/inifile/IniFile.py (line:253)


Write the IniFile content to disk
This completely overwrites the file


