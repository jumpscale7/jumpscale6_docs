

FS Walker
=========




.. code-block:: python

  WARNING:
  we need to improve the documentation on this page
  #@todo reem please check, bring up to date



dependencies:
-------------

* You'll need to apt-get python-regex first


example
-------




.. code-block:: python

  fswalker = j.base.fswalker.get()
  
  fswalker.find                       fswalker.statsAdd
  fswalker.getCallBackMatchFunctions  fswalker.statsNr
  fswalker.lastPath                   fswalker.statsPrint
  fswalker.log                        fswalker.statsSize
  fswalker.stats                      fswalker.walk




find:
^^^^^

'fswalker.find(self, root, includeFolders=False, includeLinks=False, pathRegexIncludes={}, pathRegexExcludes={}, followlinks=False, childrenRegexExcludes='.*/log/.*', '/dev/.*', '/proc/.*' <'.*/log/.*', '/dev/.*', '/proc/.*'>, mdserverclient=None)'


* root: root path to find from.
* includeFolders: defaults to False. In this case, only files are searched.
* includeLinks: defaults to False. In this case, links are not included in the search results.
* pathRegexIncludes/Excludes: match paths to array of regex expressions {[]} to be included/excluded.
* childrenRegexExcludes: Excludes children with regex matching any of the given list from the results.
* mdserverclient: To search on metadata from another server.



Example
^^^^^^^




.. code-block:: python

  fswalker.find('.', False, False, {}, {'F': ['.pyc']}, True) 
  #Finds all files that are not of type pyc listed under this directory




Walk
^^^^


'fswalker.walk(self, root, callbackFunctions={}, arg=None, callbackMatchFunctions={}, followlinks=False, childrenRegexExcludes='.*/log/.*', '/dev/.*', '/proc/.*' <'.*/log/.*', '/dev/.*', '/proc/.*'>, pathRegexIncludes={}, pathRegexExcludes={}, mdserverclient=None)'

Walk through filesystem and execute a method per file and dirname if the match function selected the item.


* root: Where to start the walk from
* callbackFunctions: callback functions to be executed to matched files/directories/links walked upon.
* arg: the first argument to be passed along to the callback function (can be used to initiate the callback function)
* callbackMatchFunctions: callback functions which control the criteria whether to select an item
* includeFolders: defaults to False. In this case, only files are walked upon.
* pathRegexIncludes/Excludes: includes everything by default. No paths are excluded. To do so, through a list of regexes.
* depths: list of depth values e.g. only return depth 0 & 1 (would mean first dir depth and then 1 more deep)
* followlinks: defaults to False, if True would follow linked files/directories to walk within them.



Complex example with regular expression find combined with call back functions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^




.. code-block:: python

  pathRegexExcludes["F"]=[".*\.pyc",".*\.bak",".*\.pyo",".*\.log"]
  childrenRegexExcludes=[".*/log/.*","/dev/.*","/proc/.*"]
  
  def processfile(path,stat,arg):
      print "%s - %s" % (path, arg)
  def processdir(path,stat,arg):
      print "%s"%path
  def processlink(path,stat,arg):
      print "%s"%path
  
  callbackFunctions={}
  callbackFunctions["F"]=processfile
  callbackFunctions["D"]=processdir
  callbackFunctions["L"]=processlink
  #callbackFunctions["O"]=processother
  #type O is a generic callback which matches all not specified (will not match F,D,L)
  
  callbackMatchFunctions=fswalker.getCallBackMatchFunctions({},pathRegexExcludes,False,False)
  
  args={}
  args["metadata"]="something"
  args["data"]="data"
  
  fswalker.walk('.',callbackFunctions,args,
                    callbackMatchFunctions,childrenRegexExcludes, 
                    [],pathRegexExcludes)




lastPath
^^^^^^^^

* fswalker.lastPath

Returns a string representation of the last object. Empty string if none found.






