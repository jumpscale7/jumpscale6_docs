
j.console
=========


* path: /core/console/Console.py


class which groups functionality to print to a console
self.width=120
self.indent=0 #current indentation of messages send to console
self.reformat=False #if True will make sure message fits nicely on screen


askArrayRow
-----------


* params: array,header,descr,returncol
* path:/core/console/Console.py (line:644)


askChoice
---------


* params: choicearray,descr,sort
* path:/core/console/Console.py (line:370)


the value of the dics is what needs to be returned, the key is the str representation


askChoiceMultiple
-----------------


* params: choicearray,descr,sort
* path:/core/console/Console.py (line:507)


askInteger
----------


* params: question,defaultValue,minValue,maxValue,retry,validate
* path:/core/console/Console.py (line:262)


Get an integer response on asked question




askIntegers
-----------


* params: question,invalid_message,min,max
* path:/core/console/Console.py (line:327)


Ask the user for multiple integers



askIpaddressInRange
-------------------


* params: question,startip,endip,network,netmask,retry
* path:/core/console/Console.py (line:558)


Ask the user to enter a valid ipaddress

Provide either startip and endip or network and netmask.



askMultiline
------------


* params: question,escapeString
* path:/core/console/Console.py (line:538)


Ask the user a question that needs a multi-line answer.



askPassword
-----------


* params: question,confirm,regex,retry,validate
* path:/core/console/Console.py (line:217)


Present a password input question to the user




askString
---------


* params: question,defaultparam,regex,retry,validate
* path:/core/console/Console.py (line:185)


Get a string response on a question




askYesNo
--------


* params: message
* path:/core/console/Console.py (line:306)


Display a yes/no question and loop until a valid answer is entered




echo
----


* params: msg,indent,withStar,prefix,log,lf
* path:/core/console/Console.py (line:109)


Display some text to the end-user, use this method instead of print
will only work when j.console.reformat==True


echoDict
--------


* params: dictionary,withStar,indent
* path:/core/console/Console.py (line:167)


echoListItem
------------


* params: msg
* path:/core/console/Console.py (line:131)


Echo a list item


echoListItems
-------------


* params: messages,sort
* path:/core/console/Console.py (line:138)


Echo a sequence (iterator, generator, list, set) as list items



echoListWithPrefix
------------------


* params: messages,prefix
* path:/core/console/Console.py (line:160)


print messages


echoWithPrefix
--------------


* params: message,prefix,withStar,indent
* path:/core/console/Console.py (line:154)


print a message which is formatted with a prefix


formatMessage
-------------


* params: message,prefix,withStar,indent,width,removeemptylines
* path:/core/console/Console.py (line:59)


Reformat the message to display to the user and calculate length


hideOutput
----------


* params:
* path:/core/console/Console.py (line:606)


rawInputPerChar
---------------


* params: callback,params
* path:/core/console/Console.py (line:22)


when typing, char per char will be returned


showArray
---------


* params: array,header
* path:/core/console/Console.py (line:609)


showOutput
----------


* params:
* path:/core/console/Console.py (line:603)


transformDictToMessage
----------------------


* params: dictionary,withStar,indent
* path:/core/console/Console.py (line:176)


