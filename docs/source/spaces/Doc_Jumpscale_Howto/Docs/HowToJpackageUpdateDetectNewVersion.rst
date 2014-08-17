

how to detect during jpackage install that its a new version
************************************************************


*@TODO could be is no longer working, needs to be verified*


* in the active hrd of the jpackage put a version field e.g.




.. code-block:: python

  elasticsearch.version=0.9.9



* when the jpackage is in prepare step, the active hrd will not be applied yet to the installed version
* so if we check for version in the prepare action we can see the installed version is different.




.. code-block:: python

  if not j.application.config.exists("elasticsearch.version") or j.application.config.get("elasticsearch.version")<>"0.9.9":
      #we are updating
      j.console.askYesNo("do you want to remove the old database of elasticsearch, this is required for this version.")
      j.system.fs.removeDirTree("/opt/data/elasticsearch/")


This will make sure that if the version does not exist yet or its different that we can do something


