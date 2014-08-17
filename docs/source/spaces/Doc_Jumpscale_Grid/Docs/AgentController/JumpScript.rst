

JumpScripts
***********


A JumpScript is a python script that can be execute on remote nodes.


Location
========


JumpScripts are located under the AgentController at '$basedir/apps/agentcontroller/jumpscripts'


Syntax.
=======


Each JumpScript corresponds to one python module and should implement one method called 'action'. This action can be paramterized.





.. code-block:: python

  from JumpScale import j
  
  descr = """
  This jumpscript echos back (test)
  """
  
  name = "echo"
  category = "test"
  organization = "jumpscale"
  author = "kristof@incubaid.com"
  license = "bsd"
  version = "1.0"
  async = False
  queue = ''
  period = 0
  roles = []
  
  
  def action(msg):
      print msg
      return msg



Attributes
----------


* name: Name of the JumpScript
* category: Category of the JumpScript
* organization: Organization of the JumpScript
* author: E-Mail address of author of the JumpScript
* license: License the JumpScript can be destributed with
* version: Version of the JumpScript
* async: Wheter to execute this JumpScript in the processmanager or on one of the workers
* queue: When queue is specified the JumpScript will be executed on the specified worker queue regardless of the async flag
* period: Interval the JumpScript will be automaticly executed at. JumpScript with interval should noet have arguments.
* roles: Roles of the node this JumpScript can be executed on. This is used for JumpScripts that have a period and also acts as a filter of which JumpScripts are loaded on each node.


