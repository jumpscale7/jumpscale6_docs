
j.gui.dialog
============


* path: /core/gui/dialog/EasyDialog.py


askChoice
---------


* params: question,choices,defaultValue,pageSize,sortChoices,sortCallBack
* path:/core/gui/dialog/EasyDialog.py (line:161)


Ask the user the supplied question and list the choices to choose from, if no response given the default value is used




askChoiceMultiple
-----------------


* params: question,choices,defaultValue,pageSize,sortChoices,sortCallBack
* path:/core/gui/dialog/EasyDialog.py (line:177)


Ask the user the supplied question and list the choices to choose from, if no response given the default values <s> is used




askDate
-------


* params: question,minValue,maxValue,selectedValue,format
* path:/core/gui/dialog/EasyDialog.py (line:202)


Asks user a question that its answer is a date between minValue and maxValue

Note: this note my seem out of place, but is is important to note that currently in the EasyDialogConsole implementation only dates with format YYYY/MM/DD are supported



askDateTime
-----------


* params: question,minValue,maxValue,selectedValue,format
* path:/core/gui/dialog/EasyDialog.py (line:217)


Asks user a question that its answer is a datetime between minValue and maxValue

Note: this note my seem out of place, but is is important to note that currently in the EasyDialogConsole implementation only dates with format YYYY/MM/DD are supported



askDirPath
----------


* params: message,startPath
* path:/core/gui/dialog/EasyDialog.py (line:93)


Prompts for a selection of a file path starting from startPath if given and '/' if not



askFilePath
-----------


* params: message,startPath
* path:/core/gui/dialog/EasyDialog.py (line:79)


Prompts for a selection of a file path starting from startPath if given and '/' if not



askForm
-------


* params: form
* path:/core/gui/dialog/EasyDialog.py (line:250)


askInteger
----------


* params: question,defaultValue
* path:/core/gui/dialog/EasyDialog.py (line:139)


Asks user the supplied question and prompt for an answer, if none given the default value is used, the response and the default value must be valid integer



askIntegers
-----------


* params: question
* path:/core/gui/dialog/EasyDialog.py (line:151)


Asks user the supplied question and prompt for an answer



askMultiline
------------


* params: question,defaultValue
* path:/core/gui/dialog/EasyDialog.py (line:193)


Asks the user the supplied question, where the answer could be multi-lines



askPassword
-----------


* params: question,confirm,regex,retry,defaultValue
* path:/core/gui/dialog/EasyDialog.py (line:130)


Asks the supplied question and prompts for password



askString
---------


* params: question,defaultValue,validator
* path:/core/gui/dialog/EasyDialog.py (line:107)


Asks the user the supplied question and prompt for an answer, if none given the default value is used


askYesNo
--------


* params: question,defaultValue
* path:/core/gui/dialog/EasyDialog.py (line:118)


Asks user the supplied question and prompt for an answer, if none given the default value is used, the response and the default value one of the values [y|Y|yes|Yes..n|N|No..]

Note:For the EasyDialogConol implementation, currently the default value effect is ignored since it would require changing the jumpscale vapp


chooseDialogType
----------------


* params: type
* path:/core/gui/dialog/EasyDialog.py (line:50)


supported types today: console,win32,wizardserver


clear
-----


* params:
* path:/core/gui/dialog/EasyDialog.py (line:253)


message
-------


* params: message
* path:/core/gui/dialog/EasyDialog.py (line:70)


prints the given message to the screen



navigateTo
----------


* params: url
* path:/core/gui/dialog/EasyDialog.py (line:247)


pm_setDialogHandler
-------------------


* params:
* path:/core/gui/dialog/EasyDialog.py (line:44)


showLogging
-----------


* params: text
* path:/core/gui/dialog/EasyDialog.py (line:241)


Shows logging message


showMessageBox
--------------


* params: message,title,msgboxButtons,msgboxIcon,defaultButton
* path:/core/gui/dialog/EasyDialog.py (line:256)


Shows a large message box




showProgress
------------


* params: minvalue,maxvalue,currentvalue
* path:/core/gui/dialog/EasyDialog.py (line:231)


Shows a progress bar according to the given values



