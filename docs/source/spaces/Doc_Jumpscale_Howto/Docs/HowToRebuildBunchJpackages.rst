

Rebuilding JPackages
====================




.. code-block:: python

  #make sure you have all most recent code
  jscode_update
  
  #to repackage code only & certain defined jpackages
  jpackage repackage --onlycode -d jumpscale -n grid*,core*,agentcon*,libs*,osis*,portal*,proces*,workers*
  
  #todo for all in domaoin jumpscale
  jpackage repackage --onlycode -d jumpscale 
  
  #now upload all jpackages (only for code recipes)
  jpackage_upload -n all -a --onlycode
  
  #now commit all your changes to repo's 
  jscode_push


