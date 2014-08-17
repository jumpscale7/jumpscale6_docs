
j.action
========


* path: /baselib/actions/action/ActionController.py


Manager controlling actions


clean
-----


* params:
* path:/baselib/actions/action/ActionController.py (line:262)


Clean the list of running actions


hasRunningActions
-----------------


* params:
* path:/baselib/actions/action/ActionController.py (line:269)


Check whether actions are currently running



printOutput
-----------


* params:
* path:/baselib/actions/action/ActionController.py (line:277)


start
-----


* params: description,errormessage,resolutionmessage,show,messageLevel
* path:/baselib/actions/action/ActionController.py (line:185)


Start a new action

fails
the action fails


startOutput
-----------


* params:
* path:/baselib/actions/action/ActionController.py (line:286)


Enable j.console output. Format such that it is nicely shown between action start/stop.


stop
----


* params: failed
* path:/baselib/actions/action/ActionController.py (line:222)


Stop the currently running action

This will get the latest started action from the action stack and
display a result message.



stopOutput
----------


* params:
* path:/baselib/actions/action/ActionController.py (line:302)


Disable j.console output. Format such that it is nicely shown between action start/stop.


