
j.gui.dialog.easyDialog
=======================


* path: /core/gui/dialog/EasyDialogConsole.py


askChoice
---------


* params: question,choices,defaultValue,pageSize,sortChoices,sortCallBack
* path:/core/gui/dialog/EasyDialogConsole.py (line:126)


Ask the user the supplied question and list the choices to choose from, if no response given the default value is used




askChoiceMultiple
-----------------


* params: question,choices,defaultValue,pageSize,sortChoices,sortCallBack
* path:/core/gui/dialog/EasyDialogConsole.py (line:169)


Ask the user the supplied question and list the choices to choose from, if no response given the default values <s> is used




askDate
-------


* params: question,minValue,maxValue,selectedValue,format
* path:/core/gui/dialog/EasyDialogConsole.py (line:318)


Asks user the supplied question, a valid answer is a date between minValue and maxValue

Currently in the EasyDialogConsole implementation ignores the format parameter and  only dates with format YYYY/MM/DD are supported



askDateTime
-----------


* params: question,minValue,maxValue,selectedValue,format
* path:/core/gui/dialog/EasyDialogConsole.py (line:178)


Asks user a question that its answer is a datetime between minValue and maxValue

Note: this note my seem out of place, but is is important to note that currently in the EasyDialogConsole implementation only dates with format YYYY/MM/DD are supported



askDirPath
----------


* params: message,startPath
* path:/core/gui/dialog/EasyDialogConsole.py (line:38)


Prompts for a selection of a file path starting from startPath if given and '/' if not



askFilePath
-----------


* params: message,startPath
* path:/core/gui/dialog/EasyDialogConsole.py (line:12)


Prompts for a selection of a file path starting from startPath if given and '/' if not



askInt
------


* params: question,defaultValue
* path:/core/gui/dialog/EasyDialogConsole.py (line:65)


Asks user the supplied question and prompt for an answer, if none given the default value is used, the response and the default value must be valid integer



askInteger
----------


* params: question,defaultValue
* path:/core/gui/dialog/EasyDialogConsole.py (line:115)


Asks user the supplied question and prompt for an answer, if none given the default value is used, the response and the default value must be valid integer



askIntegers
-----------


* params: question
* path:/core/gui/dialog/EasyDialogConsole.py (line:397)


Asks user the supplied question and prompt for an answer



askMultiline
------------


* params: question
* path:/core/gui/dialog/EasyDialogConsole.py (line:310)


Asks the user the supplied question, where the answer could be multi-lines



askPassword
-----------


* params: question,confirm,regex,retry,defaultValue
* path:/core/gui/dialog/EasyDialogConsole.py (line:88)


Asks the supplied question and prompts for password



askString
---------


* params: question,defaultValue,validator
* path:/core/gui/dialog/EasyDialogConsole.py (line:55)


Asks the user the supplied question and prompt for an answer, if none given the default value is used


askYesNo
--------


* params: question,defaultValue
* path:/core/gui/dialog/EasyDialogConsole.py (line:77)


Asks user the supplied question and prompt for an answer, if none given the default value is used, the response and the default value one of the values [y|Y|yes|Yes..n|N|No..]

Currently the default value effect is ignored since it would require changing the jumpscale vapp


chooseDialogType
----------------


* params: type
* path:/core/gui/dialog/EasyDialogConsole.py (line:434)


supported types today: console,win32,wizardserver


clear
-----


* params:
* path:/core/gui/dialog/EasyDialogConsole.py (line:441)


Clears the screen/form.


message
-------


* params: message
* path:/core/gui/dialog/EasyDialogConsole.py (line:107)


prints the given message to the screen



navigateTo
----------


* params: url
* path:/core/gui/dialog/EasyDialogConsole.py (line:393)


showLogging
-----------


* params: text
* path:/core/gui/dialog/EasyDialogConsole.py (line:386)


Shows logging message


showMessageBox
--------------


* params: message,title,msgboxButtons,msgboxIcon,defaultButton
* path:/core/gui/dialog/EasyDialogConsole.py (line:211)


Shows a message box




showProgress
------------


* params: minvalue,maxvalue,currentvalue
* path:/core/gui/dialog/EasyDialogConsole.py (line:361)


Shows a progress bar according to the given values



